from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic.base import View
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission, IsAdminUser
from django.template import engines
from wkhtmltopdf.views import PDFTemplateResponse
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
import json
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import *
from .filters import OrderFilter
from .decorators import unauthendicated_user, allowed_users, admin_only
import datetime
from django.http import HttpResponse
from django.contrib.auth.models import Group
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
from django.apps import apps
from xhtml2pdf import pisa
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .serializers import *
from rest_framework import status
from io import BytesIO
from django.shortcuts import render
from django.views import View
from django.template.loader import get_template
from rest_framework.decorators import api_view, permission_classes

User_Model = apps.get_model('products', 'User')
Customerdata_Model = apps.get_model('products', 'Customerdata')
Productdata_model = apps.get_model('products', 'Productdata')
Order_Model = apps.get_model('products', 'Order')


def home(request):
    return render(request, 'auth/index.html')

# @csrf_exempt
# @unauthendicated_user
# def signup(request):
#     form = CustomUserCreationForm()
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # cleaned_data is an object which returns validated field data
#             user = form.cleaned_data.get('username')

#             # add new user to customer group
#             group = Group.objects.get(name='customer')
#             user.groups.add(group)

#             # set new user to customer user

#             Profile = Customerdata_Model.objects.create(user=user,)
#             Profile.save()

#     context = {'form': form}
#     return render(request, 'auth/signup.html', context)


# def send_mail(request):
#     # plaintext = get_template('email.txt')
#     html = get_template('store/email3.html')

#     # d = Context({ 'username':{user.username} })

#     subject, from_email, to = 'hello', 'ellaidhurai.97@gmail.com', 'ellaidhurai.97@gmail.com'
#     text_content = 'your account is activated'
#     html_content = html.render()
#     msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()

#     return HttpResponse('success')


@csrf_exempt
@unauthendicated_user
def signup(request):

    if request.method == "POST":
        # get user input
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # check email is exist
        if User.objects.filter(email=email).first():
            messages.error(request, "email already exist!")

        try:
            # create user
            user = User(username=username, email=email,
                            password=password,)
            instance = user.save()
        except Exception as e:
            return HttpResponse(e)

        
        # add new user to customer group
        group = Group.objects.get(name='customer')
        user.groups.add(group)

        # create a customer object for new user
        user_model = User.objects.get(username=username)
        new_profile = Customerdata_Model.objects.create(user=user_model, id = user_model.id)
        new_profile.save()

        messages.success(request, 'Account created succesfully for ' + user.username)

        # send sucess email to user mail id
        subject = 'welcome to E-Kart world'
        message = f'Hi {user.username}, thank you for registering in E-Kart.'
        email_from = settings.EMAIL_HOST_USER
        email_to = [user.email, ]
        send_mail(subject, message, email_from,
                    email_to, fail_silently=False,)
    
        # navigate to login page
        # return redirect('signin')
        # render is used to render the html templates
    return render(request, "auth/signup.html")


@unauthendicated_user
def signin(request):
    if request.method == "POST":

        # get user input
        username = request.POST["username"]
        password = request.POST["password1"]

        # django default authentication
        user = authenticate(request, username=username, password=password)

        # for valid user
        if user is not None:
            # login - django default

            login(request, user)
            return redirect('user')

        # for invalid user
        username = User_Model.objects.get(username=username)

        if not username:
            messages.error(
                request, {"username": "username not match", "password1": "password not match"})

        password = User_Model.objects.filter(password=password)

        if not password:
            messages.error(request, {"password1": "password not match"})

        return redirect('signin')

    return render(request, "auth/signin.html")


def signout(request):
    logout(request)
    # messages.success(request,"You are logged out")
    return redirect('signin')


@login_required
@admin_only
def user(request):

    orders = Order_Model.objects.all()
    customers = Customerdata_Model.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'customers': customers,
        'orders': orders,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending

    }
    return render(request, "auth/user.html", context)


@login_required
@allowed_users(allowed_roles=['admin', 'customer'])
def product(request):

    products = Productdata_model.objects.all()
    return render(request, "auth/product.html", {'products': products})


@login_required
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):

    customer = Customerdata_Model.objects.get(id=pk)

    # order_set is queryset method to get child objects. customer is parent Order is child
    orders = request.user.customer_fk.order_set.all()

    # print(orders) => <QuerySet [<Order: Object1>, <Order: Object2>, <Order: Object3>, <Order: T-shirt>]>

    # print(orders.values()) => <QuerySet [{'id': 1, 'customer_fk_id': 1, 'Product_fk_id': 1, 'CreatedDate': datetime.date(2023, 1, 13), 'status': 'Delivered', 'quantity': 9, 'note': 'urgent'},{},{}...]

    li = [o for o in orders.values()]
    # values() method returns array of dict
    # print(li) =>  [{'id': 1, 'customer_fk_id': 1, 'Product_fk_id': 1, 'CreatedDate': datetime.date(2023, 1, 13), 'status': 'Delivered', 'quantity': 9, 'note': 'urgent'},]
    # print(li[0]['id']) => 1 ,access value of dict object

    li = []
    for price in orders:
        total_price = price.Product_fk.Price
        li.append(total_price)

    total = sum(li)

    order_count = orders.count()
    filter = OrderFilter(request.GET, queryset=orders)

    # filter items based on queryset
    orders = filter.qs

    context = {'customer': customer, 'orders': orders,
               'order_count': order_count, "filter": filter}
    return render(request, "auth/customer.html", context)


@login_required
@allowed_users(allowed_roles=['admin'])
def create_order(request, pk):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer_fk = request.user
            instance.save()
            return redirect('user')

    customer = Customerdata_Model.objects.get(id=pk)
    order_form = OrderForm(initial={'customer': customer})
    context = {'form': order_form}
    return render(request, "auth/order-form.html", context)


@login_required
@admin_only
def update_order(request, pk):

    orders = Order_Model.objects.get(id=pk)

    # Here we use POST method instead PUT method because html forms only supports GET and POST methods
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=orders)

        if form.is_valid():
            form.save()
            return redirect('user')

    update_form = OrderForm(instance=orders)
    context = {'form': update_form}
    return render(request, "auth/order-form.html", context)


@login_required
@admin_only
def delete_order(request, pk):
    Order_Model = apps.get_model('products', 'Order')
    order = Order_Model.objects.get(id=pk)

    # Here we use POST method instead DELETE method because html forms only supports GET and POST methods
    if request.method == 'POST':
        order.delete()
        return redirect('user')

    context = {'item': order}
    return render(request, "auth/delete-form.html", context)


@login_required
@allowed_users(allowed_roles=['customer', 'admin'])
def userPage(request):
    # query to find logged in user's orders
    orders = request.user.customer_fk.order_set.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {
        'orders': orders,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
    }
    return render(request, 'auth/profile.html', context)


# allowed groups
@login_required
@allowed_users(allowed_roles=['customer', 'admin'])
def accountSettings(request):
    # find logged in user
    customer = request.user.customer_fk
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'auth/account-settings.html', context)


def time(request):
    time = datetime.datetime.now()
    return HttpResponse(time)


@login_required
# @permission_required('products.can_view_post') # django permission checking decorator
def CustomerPostGroup(request):

    # if request.user.groups.filter(name = 'customer').exists():
    if request.user.has_perm('products.can_view_post'):
        Post_Model = apps.get_model('products', 'Post')
        Posts = Post_Model.objects.all()
        return render(request, 'auth/account_settings.html', {'Post': Posts})
    else:
        return HttpResponse("only for customer group")


def LoadReactPage(request):
    a = {
        "username": "ellai"
    }
    return render(request, 'auth/react.html', a)

 # custom permission through code
# from django.contrib.auth.models import Group, ContentType, Permission
# ct = ContentType.objects.get_for_model(Post)
# permission = Permission.objects.create(codename='can_view_post', content_type=ct)


# adding permission to one user
# user.permissions.add(permission)

# adding permission to group
# new_group, created = Group.objects.get_or_create(name='new_group')
# new_group.permissions.add(permission)

# text to html convertion


def Text_Html(request):
    form = EditorForm()
    return render(request, 'auth/text-to-html.html', {'form': form})

from django.db.models import Q
@login_required
# ecom
def store(request):
    if request.user.is_authenticated:

        customer = request.user.customer_fk
        customer_orders = customer.order_set.all()
        
        # ~Q not 
        data = Order.objects.filter(Q(status='Pending') | ~Q(status='Delivered'))
        # print(data)
        value = []
        for i in customer_orders:
            value.append(i.quantity)

        total_quantity = sum(value)

    else:
        customer_orders = []

    products = Productdata_model.objects.all()
    context = {'products': products, 'total_quantity': total_quantity}
    return render(request, 'store/store.html', context)


@login_required
def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer_fk
        customer_orders = customer.order_set.all()
        total_items = customer_orders.count()
    else:
        customer_orders = []

    list = []
    list2 = []
    
    for i in customer_orders:
        quantity = i.quantity 
        list2.append(quantity)
        list.append(i.quantity * i.Product_fk.Price)
 
    total_price = sum(list)
    total_quantity = sum(list2)
    
    context = {
        "customer_orders": customer_orders,
        "total_items": total_items,
        "total_quantity": total_quantity,
        "total_price": total_price
    }
    return render(request, 'store/cart.html', context)


@login_required
def checkout(request):
   
    if request.user.is_authenticated:
        customer_orders = request.user.customer_fk.order_set.all()
        total_items = customer_orders.count()
        
    else:
        customer_orders = []
    
    list = []
    list2 = []
    
    for i in customer_orders:
        
        quantity = i.quantity 
        list2.append(quantity)
        list.append(i.quantity * i.Product_fk.Price)
 
    total_price = sum(list)
    total_quantity = sum(list2)

    shipping = False
    for i in customer_orders:
        # print(i.Product_fk.digital)
        if i.Product_fk.digital == False:
            shipping = True

    context = {
        "customer_orders": customer_orders,
        "total_items": total_items,
        "total_price": total_price,
        "total_quantity": total_quantity,
        "shipping": shipping
    }

    return render(request, 'store/checkout.html', context)


@login_required
def updateItem(request):

    # convert request data to json
    data = json.loads(request.body)
    # get the request data
    productId = data['productId']
    action = data['action']

    customer = request.user.customer_fk
    product = Productdata_model.objects.get(id=productId)

    # get_or_created method is used to create new order

    orderItem, created = Order_Model.objects.get_or_create(
        customer_fk=customer, Product_fk=product)
    print(orderItem)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity+1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity-1)

        # when customer changes the quantity save that changes in db
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def exercise(request):
    return render(request, "store/exercise.html")


def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'auth/upload.html', {'file_url': file_url})
    return render(request, 'auth/upload.html')


def html_to_pdf(template_src, context_dic={}):
    template = get_template(template_src)
    html = template.render(context_dic)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        data = Template.objects.all().order_by('student_name')
        open('templates/temp.html',
             "w").write(render_to_string('store/email2.html', {'data': data}))

        pdf = html_to_pdf('temp.html')
        return HttpResponse(pdf, content_type='application/pdf')


class DownloadPDF(View):
    def get(self, request, *args, **kwargs):

        pdf = html_to_pdf('temp.html')

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Template_%s.pdf" % ('12341231')
        content = "attachment; filename = '%s'" % (filename)
        response['Content-Disposition'] = content
        return response


@api_view(['POST'])
def create_tc(request):
    serializers = TemplateSerializers(data=request.data)
    try:
        if serializers.is_valid():
            serializers.save()
        return Response(serializers.data)
    except Exception:
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def view_tc(request):
    try:
        student = Template.objects.all()
        studentdata = [data for data in student]

    except Exception:
        return Response('no data', status=status.HTTP_400_BAD_REQUEST)

    context = {
        'studentdata': studentdata,

    }

    return render(request, 'store/email.html', context)



def view_react(request):
    return render(request, 'auth/react.html')