from django.views.decorators.csrf import csrf_exempt  # cors
from rest_framework.response import Response
from products.models import Productdata, Customerdata,User,Post
from products.serializers import ProductdataSerializers, CustomerdataSerializers,UserSerializer,AccessTokenPairSerializer,PostSerializers
from rest_framework.decorators import api_view, permission_classes  
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission,IsAdminUser
from rest_framework import viewsets
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from rest_framework.viewsets import GenericViewSet
from django.shortcuts import get_object_or_404
import requests
from rest_framework_simplejwt.views import TokenObtainPairView
from .permissions import isAdmin
from django.contrib.auth.models import Group


# private_api_url = 'http://127.0.0.1:8000/'
# private_api_url = 'http://127.0.0.1:8000/o/token/'
   
# @api_view(['POST'])
# # @permission_classes([BasePermission.has_permission])
# def token(request):
#     '''
#     Gets tokens with username and password. Input should be in the format:
#     {"username": "username", "password": "1234abcd"}
#     '''
#     r = requests.post(private_api_url + 'o/token/',
#         data={
#             'grant_type': 'password',
#             'username': request.data['username'],
#             'password': request.data['password'],
#             'client_id': CLIENT_ID,
#             'client_secret': CLIENT_SECRET,
#         },
#     )
#     return Response(r.json())



class AccessTokenObtainPairView(TokenObtainPairView):
    serializer_class = AccessTokenPairSerializer


@permission_classes([IsAuthenticated,isAdmin])
class CustomUserViewSet(GenericViewSet):
    # By using the “self” we can access the attributes and methods of the class in GenericViewSet.
    def list(self, request):        
        try:
           queryset = User.objects.all()
           serializer = UserSerializer(queryset, many=True) 
        except:
            return Response({"message":"token not found"}, status=status.HTTP_400_BAD_REQUEST) 
        
        return Response(serializer.data, status=status.HTTP_200_OK) # json data
        
    
    def create(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk=None):
        pass
    
    def destroy(self, request, pk=None):
        pass
    
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    
    
    
    
    
    
    
    
# function based api view
    
 # product view   
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated,isAdmin])
def ProductdataApi(request):
    if request.method == 'GET':
        try:
           product_data = Productdata.objects.all() 
        except:
            return Response({"message":"no data"}, status=status.HTTP_400_BAD_REQUEST) 

        serializer = ProductdataSerializers(product_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) # json data
    
    elif request.method == 'POST':        
        serializer = ProductdataSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
# customer view

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])    
def CustomerdataApi(request):
    if request.method == 'GET':
        userdata = Customerdata.objects.all() # sql data
        serializer =CustomerdataSerializers(userdata, many=True)
        return Response(serializer.data) # json data
    
    elif request.method == 'POST':
        serializer = CustomerdataSerializers(data=request.data)
        # check serializer is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# get one data
@api_view(['GET',])
@permission_classes([IsAuthenticated])    
def CustomerSingledata(request,pk):
        userdata = Customerdata.objects.get(id=pk) # sql data
        serializer =CustomerdataSerializers(userdata, many=False)
        return Response(serializer.data) # json data    
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated,isAdmin])    
def CustomerUpdate(request,pk):
        oneuser = Customerdata.objects.get(id=pk)
        serializer = CustomerdataSerializers(instance=oneuser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])    
def CustomerDelete(request,pk):
        oneuser = Customerdata.objects.get(id=pk)
        oneuser.delete    
        return Response("deleted successfully")
  

# Post view
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])    
def BlogApi(request):
    if request.method == 'GET':
        userdata = Post.objects.all() # sql data
        serializer =PostSerializers(userdata, many=True)
        return Response(serializer.data) # json data
    
    elif request.method == 'POST':
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])    
def BlogMethodApi(request,pk):
    if request.method == 'PUT':
        onepost = Post.objects.get(id=pk)
        serializer = PostSerializers(instance=onepost,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        onepost = Post.objects.get(id=pk)
        onepost.delete
        
        return Response("deleted successfully")

















