from distutils.log import error
from email import message
from multiprocessing import context
from unicodedata import category
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Category,Order,Product,Customer
from .forms import OrderForms,CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user , admin_only, allowed_users

#sql -> select all from categories
#Orm -> object relational model


# Create your views here.
@unauthenticated_user
def user_registration(request):

        form = CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('/')
            else:
                messages.info(request,'Validation Failed')



        context = {
            "form":form,
        }
        return render(request,'register.html',context=context)

@unauthenticated_user
def user_login(request):


        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.info(request,"Username or Password is incorrect")

        context={}
        return render(request,'login.html',context=context)




def user_logout(request):
    logout(request)
    return redirect('login')


def index(request):
    categories= Category.objects.all()
    context={
        "categories":categories,

    }


    return render(request,"index.html", context=context)





def about(request):
    return render(request,"about.html")


@login_required(login_url='login')
def order(request):

    forms = OrderForms()

    if request.method=="POST":
        forms=OrderForms(request.POST)
        if forms.is_valid:
            forms.save()
            return redirect('order_list')

    context={
        "forms":forms,
    }


    return render(request,"order.html",context=context)

def sign_in(request):
    return render(request,"sign_in.html")

@login_required(login_url='login')
def order_list(request):
    orders = Order.objects.all()
    context={
        "order_list":orders,
    }

    return render(request,"order_list.html", context=context)


def show_category(request, pk):
    category = Category.objects.get(id=pk)

    context = {
        "category": category,
    }

    print(category)

    return render(request, "category_details.html", context=context)

@allowed_users(allowed_roles=['admin','Manager'])
def update_order(request, pk):
    order = Order.objects.get(id=pk)
    forms = OrderForms(instance=order)

    if request.method == 'POST':
        forms = OrderForms(request.POST, instance=order)
        if forms.is_valid():
            forms.save()
            return redirect('order_list')

    context = {
        'forms': forms
    }
    return render(request, 'order.html', context=context)

def show_order(request, pk):
    order_details = Order.objects.get(id=pk)

    context = {
        'order': order_details,
    }

    return render(request, 'order_details.html', context=context)


def delete_order(request, pk):
    item = Order.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('order_list')

    context = {
        'item': item,
    }

    return render(request, 'delete.html', context=context)

      

