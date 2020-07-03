from django.shortcuts import render, redirect
from Customer.forms import *
from Customer.models import Customer
from Vendor.models import Book
# Create your views here.

def CustomerReg(request):
    form=CustomerRegForm()
    template_name="customer/register/registration.html"
    context={}
    context['customerreg']=form
    if request.method=="POST":
        form=CustomerRegForm(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved")
            return redirect('login')

    return render(request,template_name,context)

def customerLogin(request):
    form=CustomerLoginForm()
    template_name="customer/login/login.html"
    context={}
    context['customerlogin']=form
    if request.method=="POST":
        loginfrm=CustomerLoginForm(request.POST)
        print("Posted")
        if loginfrm.is_valid():
            print("Valid")
            name=loginfrm.cleaned_data['username']
            pwd=loginfrm.cleaned_data['password']
            ob=Customer.objects.get(username=name)
            if((ob.username==name) & (ob.password==pwd) ):
                print("Login successful")
                request.session["user"]=name
                return redirect('homepage')
            else:
                loginfrm = CustomerLoginForm(request.POST)
                context={}
                context['customerlogin']=loginfrm
                template_name = "customer/login/login.html"
                return render(request,template_name,context)

    return render(request,template_name,context)

def customerHome(request):
    data=Book.objects.all()
    template_name="customer/home/home.html"
    context={}
    context['book']=data
    return render(request,template_name,context)

def baseTemp(request):
    template_name="customer/base.html"
    return render(request,template_name)

def viewBook(request,pk):
    qs=Book.objects.get(id=pk)
    template_name="customer/books/bookview.html"
    context={}
    context['bookview']=qs
    return render(request,template_name,context)