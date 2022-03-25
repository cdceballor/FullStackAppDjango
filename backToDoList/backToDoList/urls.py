"""backToDoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers #Import the routes
from todo import views #Todo is the name of the project, could be other if you prefer

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo') #The r'todos' is the extension of the path in the search bar in internet, in other words: localhost:8000/api/todos <- this todos, second parameter is the view class

urlpatterns = [
    path('admin/', admin.site.urls),
        path('api/', include(router.urls)), #Creating url to the view

]
