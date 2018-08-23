from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registerValidator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = 'Name must be at least 2 charachters long'
        if  len(postData['alias']) < 2:
            errors['alias'] = 'Alias must be at least 2 charachters long'
        if len(postData['email']) < 1 or not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'You must enter a valid email address'
        else:
            try:
                User.objects.get(email = postData['email'])
                errors['email_exists'] = 'This email already exists'
            except User.DoesNotExist:
                pass
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 charachters long'
        if postData['confirm_pw'] != postData['password']:
            errors['confirm_pw'] = 'Your passwords must match'
        return errors
    
    def loginValidator(self, postData):
        errors = {}
        try:
             user = User.objects.get(email = postData['login_email'])
        except User.DoesNotExist:
            errors['login_error'] = 'Unsuccessful login, please check email/password and try again.'
            return errors
        if not bcrypt.checkpw(postData['login_password'].encode(), user.password.encode()):
            errors['login_error'] = 'Unsuccessful login, please check email/password and try again.'
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 


class Review(models.Model):
    user = models.ForeignKey(User, related_name="reviewed_books")
    book = models.ForeignKey(Book, related_name="book_reviews")
    review = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
