from tkinter import CASCADE
from unicodedata import name
from django.db import models

# Create your models here.


class Author(models.Model):
    name=models.CharField(max_length=200)

class Post(models.Model):
    title=models.CharField(max_length=200, verbose_name='Title')
    text=models.TextField(verbose_name='Text')
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    created_date=models.DateTimeField(verbose_name="Created_date")
    published_date=models.DateTimeField(verbose_name='Published_date')

