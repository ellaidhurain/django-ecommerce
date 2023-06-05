# from rest_framework.response import Response
from django.shortcuts import redirect
from django.http import HttpResponse
from rest_framework import status
from functools import wraps 
import time
import logging

def unauthendicated_user(view_func):
    @wraps(view_func)
    def wrapper_func(request, *args, **kwargs):
        # if user is already logged in dont show login page
        
        if request.user.is_authenticated:
            return redirect('user')
        # if user is not logged in navigate to login page
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


# show pages besed on allowed roles
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper_func(request, *args, **kwargs):
            
            # find user is exist in group
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            # if user in group has permission return user page based on roles
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
                
            # else not allow user
            else:
                return HttpResponse('you are not authorized to view this page')
        return wrapper_func
    return decorator


def admin_only(view_func):
    @wraps(view_func)
    def wrapper_func(request, *args, **kwargs):
            customer_orders  = request.user.customer_fk.order_set.all()
            # if customer_orders[0].status == 'Pending':
            #     return HttpResponse('unauthorized')
            
            # find user is exist in group
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
             
             # if user is in 'customer' group redirect to userPage
            if group == 'customer':
                return redirect('store')        
            
            # if user is in 'admin' group return admin page
            else:
                return view_func(request, *args, **kwargs)
    return wrapper_func

# wrapper function is executed first
# when wrapper function executed it returns view_func()

def my_timer(view_func):
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = view_func(*args, **kwargs)
        t2 = time.time() - t1

        print('{} ran in: {}'.format(view_func.__name__, t2))
        return result    
    return wrapper


def my_logger(view_func):
    logging.basicConfig(filename='{}.log'.format(view_func.__name__), level=logging.INFO)
    
    @wraps(view_func) # with this decorator we can stack multiple decorators in single function without any problem
    def wrapper(*args, **kwargs):
        logging.info(
        'Ran with args: {}, and kwargs:{}'.format(args, kwargs)
        )
        return view_func(*args, **kwargs)
    
    return wrapper


# @my_logger
# @my_timer
# def display_info(name,age):
#     time.sleep(1) # Python time sleep function is used to add delay in the execution of a program.
#     print('{},{}'.format(name,age))

# display_info('ellai', 25)  
 


# decorated_display = decorator_function(display) # => @decorator_function
# decorated_display() # here we executing our wrapper function

# takes o positional arguments but 2 were given error => *args is the solution

