from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    uploader  = models.ForeignKey(User,related_name='uploaded_books')
    liked_by = models.ManyToManyField(User,related_name='liked_books')