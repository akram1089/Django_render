from django.db import models

# Create your models here.
import uuid
from django.db import models

# Create your models here.
class StudentData(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    roll_num=models.CharField( max_length=50)
    stream=models.CharField( max_length=50)

    def __str__(self):
     return self.name
    