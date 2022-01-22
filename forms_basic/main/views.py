from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def test(response):
    return HttpResponse("<h1>Hello Friends</h1>")
def v1(response):
    return HttpResponse("<h1>View 1!</h1>")
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})
def create(response):
    if response.method == "POST":
        form= CreateNewList(response.POST)
        if form.is_valid():
            n=form.cleaned_data["name"]
            t=ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form=CreateNewList()
    return render(response, "main/create.html", {"form":form})