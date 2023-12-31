from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_pics', default='default.jpg')

    def __str__(self):
        return f"@{self.user.username}"

    def save(self, *args, **kwargs):
        kwargs['force_insert'] = False  # устанавливаем значение force_insert
        super().save(*args, **kwargs)
        img = Image.open(self.avatar.path)

        if img.height >300 or img.width > 300:
            img.thumbnail((300,300))
            img.save(self.avatar.path)
