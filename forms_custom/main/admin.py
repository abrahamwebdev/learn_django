from django.contrib import admin

# Register your models here.
from .models import Item, ToDoList
admin.site.register(ToDoList)
admin.site.register(Item)