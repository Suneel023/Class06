from django.shortcuts import render
from django.http import HttpResponse
from math import factorial

# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to Views of MyApp</h1>")

def home(request):
    return render(request,"myapp/home.html",{'name':"Sunil"})

def fact(request,n):
    n=int(n)
    return HttpResponse("<h4>factorial of {} is {}</h4>".format(n,factorial(n)))

def base(request):
    return render(request,"myapp/base.html")

def child(request):
    return render(request,"child.html")

