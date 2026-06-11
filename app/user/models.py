from django.db import models

# Create your models here.

class Subscription (models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    duration = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name   


class User (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.IntegerField

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return self.name


class UserSubscription(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL,null=True)
    
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name + " " + self.subscription.name   
