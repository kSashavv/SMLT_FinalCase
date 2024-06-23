from django.db import models


class Images(models.Model):
    #id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='images/')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class ImagesModel(models.Model):
    #id = models.AutoField(primary_key=True)
    img_model = models.ImageField(upload_to='images/')
    image = models.OneToOneField(Images, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)