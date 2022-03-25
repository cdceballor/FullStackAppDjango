from django.db import models

# Create your models here.

class Todo(models.Model):
    #Create the files
    title= models.CharField(max_length=120)
    description= models.TextField()
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.title