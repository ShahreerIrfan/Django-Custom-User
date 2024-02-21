from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .constant import BLOOD_GROUP,GENDER

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bloodGroup = models.CharField(max_length=10, choices=BLOOD_GROUP)
    birthDate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER)
    image = models.ImageField(upload_to='users/images/', null=True, blank=True)  # New field for user image
    
    def __str__(self):
        return f'{self.user.username}'

class UserAddress(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,related_name ='address')
    streetAddress = models.CharField(max_length = 40)
    postalCode = models.IntegerField()
    country = models.CharField(max_length = 40)

    def __str__(self) -> str:
        return f'Address of {self.user.username}'


