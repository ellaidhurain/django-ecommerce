from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import CustomUserViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, re_path
from django.views.generic import TemplateView



# create url path here
urlpatterns = [

    # my url
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    # path('ecom/', include('store.urls')),
    path('api/products/',include('products.urls')),
    
    # rest_framework page url
    path('api/auth/', include('rest_framework.urls')),

    
    # oauth2 token 
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    
    path('google_auth', TemplateView.as_view(template_name='store/main.html')),
    path('accounts/', include('allauth.urls')),
  
 
]


router = DefaultRouter()  # assign to variable router
# create router for user view
router.register('custom_user', CustomUserViewSet, basename='custom_user') # create router for user view

urlpatterns += router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)