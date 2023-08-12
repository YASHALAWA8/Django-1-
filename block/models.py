from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

class Article(models.Model):
    title = models.CharField(max_length=255)
    # sumary  = models.CharField(max_length=255)
    full_text = models.TextField()
    category = models.CharField(max_length=255)
    pubdate = models.DateTimeField(auto_now=True)
    # slug = ... #TODO
    # is_publoshed = models.BooleanField() #TODO
    def __str__(self):
        return self.title


class OtherText(models.Model):
    title = models.CharField(max_length=255, default='Unknown')
    text = RichTextField()
    def __str__(self):
        return self.title