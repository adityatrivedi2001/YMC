from django.db import models

class HomeImages(models.Model):
    img = models.ImageField(upload_to='assests/upload')

# class events(models.Model):
#     date = models.DateTimeField()
#     title = models.CharField(max_length=25)
#     desc = models.CharField(max_length=100)


