from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from io import BytesIO
from PIL import Image
import os
import qrcode
from django.core.files import File


class Profile(models.Model): 
    image = models.ImageField(upload_to='profile_images/')
    name = models.CharField(max_length=50)
    checkedin = models.DateField()
    sex = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    medications = models.TextField()
    Latest_diagnosis = models.CharField(max_length=50) #latest diagnosis
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
    

