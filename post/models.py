from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title