from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import ProductForm, LoginForm
from .models import Product_Detail
from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def Login(request):
    if request.method == 'GET':
        context = {}
        context['form'] = LoginForm()
        return render(request, 'Login.html', context)
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/product_list')
            else:
                return redirect('/')
    
def List_Products(request):
    all_products = Product_Detail.objects.all() 
    return render(request, 'Product_Page.html', {'all_products': all_products})

def Create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/product_list')
        else:
            return redirect('/create_product')
    else:
        form = ProductForm()
    return render(request, 'Product_Create_Form.html', {'form': form})

def Edit_Product(request, id):
    if id == None:
        return redirect('/product_list')
    else:
        product_value = get_object_or_404(Product_Detail, id=id)
        if request.method == 'GET':
            context = {'form': ProductForm(instance=product_value), 'id' : id}
            return render(request, 'Product_Create_Form.html', context)
        elif request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product_value)
            if form.is_valid():
                form.save()
                return redirect('/product_list')
            else:
                return render(request, 'Product_Create_Form.html', {'form': form})
            
def Delete_Product(request, id):
    del_id = Product_Detail.objects.get(id=id)
    del_id.delete()
    return redirect('/product_list')