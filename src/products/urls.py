from django.urls import re_path,path,include
from products import views
from .views import AccessTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from products import exercise
from products import oop
from products import json
from products import youtube

urlpatterns = [
    # product url
    path('product_data', views.ProductdataApi, name='product'), # get , post , update ,delete
    re_path(r"^product/([0-9]+)$", views.ProductdataApi), # delete by id

    # customer url
    path('customer_data', views.CustomerdataApi, name='customer'),
    path('get_one_customer/<str:pk>/', views.CustomerSingledata, name='get_one_customer'), #get one data
    path('update_one_customer/<str:pk>/', views.CustomerUpdate, name='update_one_customer'), #update one data
    path('delete_one_customer/<str:pk>/', views.CustomerDelete, name='delete_one_customer'), #delete one data
    re_path(r"^customer/([0-9]+)$", views.CustomerdataApi),  #single root url with multiple method 
    
    #blog url
    path('getAllBlogs', views.BlogApi, name='getAllBlogs'),
    path('putAllBlogs', views.BlogMethodApi, name='getAllBlogs'),
    
        
    # auth token url
    path('token/', AccessTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
]


