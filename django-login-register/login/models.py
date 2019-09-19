# coding: utf8
from django.db import models

# Create your models here.
class User(models.Model):
    gender = (
        ('male', 'man'),
        ('female', 'woman'),
    )
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    c_time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='man')
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-c_time']
        verbose_name = 'user'
        verbose_name_plural = 'user'


class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ':' + self.code

    class Meta:
        ordering=['-c_time']
        verbose_name = 'code'
        verbose_name_plural = 'code'


