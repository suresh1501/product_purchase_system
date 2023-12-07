from django import forms
from django.forms import TextInput, NumberInput, PasswordInput, EmailInput
from .models import Product_Detail, User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, widget=EmailInput(attrs={'type': 'email', 'placeholder': 'Enter Email', 'class': 'form-control'}))
    username = forms.CharField(required=True, widget=TextInput(attrs={'type': 'text', 'placeholder': 'Enter Username', 'class': 'form-control'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Enter Password', 'class': 'form-control'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Confirm Password', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=TextInput(attrs={'type': 'text', 'placeholder': 'Enter User Name', 'class': 'form-control'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Enter Password', 'class': 'form-control'}))
    
class ProductForm(forms.ModelForm):
    product_name = forms.CharField(required=True, widget=TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Enter Product Name', 'style': 'width: 60%'}))
    product_price = forms.IntegerField(required=True, widget=NumberInput(attrs={'class': 'form-control', 'type': 'number', 'placeholder': 'Enter Price', 'style': 'width: 60%'}))
    product_image = forms.ImageField()
    
    class Meta:
        model = Product_Detail
        fields = ['product_name', 'product_price', 'product_image']