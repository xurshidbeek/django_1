from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=106)
    description = models.TextField()
    author = models.CharField(max_length=109)
    count = models.PositiveIntegerField()
    price = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class Author(models.Model):
    ism = models.CharField(max_length=150)
    sana = models.PositiveIntegerField


