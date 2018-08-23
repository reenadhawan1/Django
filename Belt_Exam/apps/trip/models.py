from django.db import models
import re
from datetime import date
from datetime import datetime
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registerValidator(self, postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors['first_name'] = 'First name must be at least 2 charachters long'
        if  len(postData['last_name']) < 2:
            errors['last_name'] = 'Last Name must be at least 2 charachters long'
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

    def tripValidator(self, postData):
        errors = {}
        today = datetime.combine(date.today(), datetime.min.time())
        from_date = datetime.strptime(postData['from'],'%Y-%m-%d')
        to_date = datetime.strptime(postData['to'],'%Y-%m-%d')
        if len(postData['dest']) < 1 or len(postData['desc']) < 1:
            errors['dest-desc'] = 'A destination and description is required'
        if len(postData['to']) < 1 or len(postData['from']) < 1:
            errors['dates'] = 'All dates must be entered.'
        if from_date <= today:
            errors['from'] = f'The start date must be in the future.(after {today})'
            print(postData['from']) 
        if to_date <= from_date:
            errors['to'] = f'The Date To must be after the Date From ({from_date})'
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Trip(models.Model):
    planner = models.ForeignKey(User, related_name='created_trip')
    trip_members = models.ManyToManyField(User, related_name="joined_trips")
    destination = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()

