from django.contrib import admin
from .models import Customerdata,Productdata,User,Type,Order,Post,ShippingAddress
from django.contrib.auth.admin import UserAdmin 
from django.forms import Textarea, TextInput


class UserAdmin(UserAdmin):
  search_fields = ('email','username',)
  list_filter = ('email','username',)
  ordering = ('-date_joined',)
  list_display = ('email','username','is_active','is_user','is_admin','is_superuser',)
  fieldsets = (
    (None,{'fields':('email','username',)}),
    ('Permissions',{'fields':('is_user','is_active','is_admin','is_superuser',)}),
    ('Group Permissions', {
    'fields': ('groups', 'user_permissions', )
  })
  )

  add_fieldsets = (
    (None,{
      'classes':('wide',),
      'fields':('email','username','password1','password2','is_user','is_active','is_admin','is_superuser',)
    }),
    
  )


class AuthorAdmin(admin.ModelAdmin):
  list_display = ('title','description')

admin.site.register(User,UserAdmin)
admin.site.register(Post, AuthorAdmin)
admin.site.register(Customerdata)
admin.site.register(Productdata)
admin.site.register(Type)
admin.site.register(Order) 
admin.site.register(ShippingAddress) 