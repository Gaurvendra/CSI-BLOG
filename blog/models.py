from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.
class post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    auther =models.ForeignKey(User, on_delete=models.CASCADE)
    head_image=models.ImageField(default='default1.jpg',upload_to='blog_pic')
    category = models.CharField(max_length=100)

    def __str__(self):

        return self.title

    def get_absolute_url(self):
        return reverse ('blogpost', kwargs ={'id': self.id})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.head_image.path)
        if img.height > 600 or img.width > 600:
            s = (600, 600)
            img.thumbnail(s)
            img.save(self.head_image.path)


