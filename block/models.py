from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User


class OtherText(models.Model):
    title = models.CharField(max_length=255, default='Unknown')
    date_time = models.DateField(auto_now_add=True)
    text = RichTextField()
    likes = models.ManyToManyField(User, related_name="blog_post")

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey("OtherText",on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)
