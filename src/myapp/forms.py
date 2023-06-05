from django.forms import ModelForm
from .models import *
from products.models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from products.models import User, Customerdata
from django import forms

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
 
class CustomUserCreationForm(UserCreationForm):
    
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control'}))
 
    class Meta:
        model = User
        fields = ('username','email','password1','password2')


class CustomerForm(ModelForm):
    class Meta:
        model = Customerdata
        fields = '__all__'
        exclude = ['user']
        
        


# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = User
#         fields = ('username','email','password1','password2')




from .models import Editor
from ckeditor.widgets import CKEditorWidget

class EditorForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(),label="Text Editor")
    class Meta:
        model=Editor
        fields="__all__"