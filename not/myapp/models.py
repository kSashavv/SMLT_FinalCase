from django.db import models
from django.contrib.auth.models import User


class Images(models.Model):
    img = models.ImageField(upload_to='images/')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class ImagesModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img_model = models.ImageField(upload_to='images/')
    image = models.OneToOneField(Images, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
