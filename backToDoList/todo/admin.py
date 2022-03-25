from django.contrib import admin
from .models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "completed", "date")
    
admin.site.register(Todo, TodoAdmin) #Creating connection to the admin and the app
