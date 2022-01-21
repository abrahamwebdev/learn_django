from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.
def test(response):
    return HttpResponse("<h1>Hello Friends</h1>")
def v1(response):
    return HttpResponse("<h1>View 1!</h1>")
def index(response,id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})