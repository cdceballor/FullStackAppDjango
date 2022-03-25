from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta: #Creating metadata
        model=Todo #Creating the model of the metadata
        fields=('id', 'title', 'description', 'completed', 'date') #Creating the fields of the metadata