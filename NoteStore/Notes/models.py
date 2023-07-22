from django.db import models
from django.contrib.auth.models import User
class Note(models.Model):
    title=models.CharField( max_length=50,null=False)
    description=models.TextField(null=False)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    

# Create your models here.
