from django.db import models

# Create your models here.

class Student(models.Model):
    ScholarNo=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=100)
    Clas=models.CharField(max_length=100)
    Section=models.CharField(max_length=20)
    Photo=models.ImageField(upload_to='one/images/')
    
