from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=15)
    role = models.CharField(max_length=15)
    username = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.email


class Doctor(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=15)
    address = models.TextField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    profile_pic = models.ImageField(max_length=100,upload_to='media/upload')

    def __str__(self) -> str:
        return self.firstname

class Patient(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=15)
    address = models.TextField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    profile_pic = models.ImageField(max_length=100,upload_to='media/upload')

    def __str__(self) -> str:
        return self.firstname