from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from myapp import decorators

urlpatterns = [
    path('',views.signin, name='signin'),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('user', views.user, name="user"),
    path('userPage', views.userPage, name="userPage"),
    path('product', views.product, name="product"),
    path('delete_product/<int:product_id>', views.delete_product, name="delete_product"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('customer/<str:pk>/create_order', views.create_order, name="create_order"),
    path('customer/<str:pk>/update_order', views.update_order, name="update_order"),
    path('customer/<str:pk>/delete_order', views.delete_order, name="delete_order"),
    path('account/', views.accountSettings, name="account"),
    path('account/CustomerPostGroup/', views.CustomerPostGroup, name='CustomerPostGroup'),

    path('LoadReactPage', views.LoadReactPage, name='LoadReactPage'),
    
    path('Text_Html', views.Text_Html, name="Text_Html"),
    path('pdf_view/', views.ViewPDF.as_view(), name='pdf_view'),
    path('pdf_download/', views.DownloadPDF.as_view(), name='pdf_download'),
    path("send_mail", views.send_mail, name='send_mail'),
    
    path('create_tc', views.create_tc, name='create_tc'),
    path('view_tc', views.view_tc, name='create_tc'),
    
    path('exercise/', views.exercise, name="exercise"),
    path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('updateItem/', views.updateItem, name="updateItem"),
 
    path("upload", views.upload, name="upload"),
    path('react' ,views.view_react ),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),    
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
