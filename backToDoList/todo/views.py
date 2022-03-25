from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer #Import the class TodoSerializer by serializers
from .models import Todo #Import the class Todo by models
# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer #Creating an extension of the serializer class
    queryset = Todo.objects.all() #Create the query to all the Todo objects