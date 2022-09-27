from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view1(request, *args,**kwargs):
  print(args,kwargs)
  print(request.user)
  return HttpResponse("<h1>Hello World</h1>")

def contact_view(request,*args,**kwargs):
  return render(request,"contact.html",{})

def home_view(request,*args,**kwargs):
  return render(request,"home.html",{})


def about_view(request,*args,**kwargs):
  my_context ={
    "my_text":"This is me learning",
    "my_number":"1234",
    "my_list":[1,2,3,4]

  }
  return render(request,"about.html",my_context)