# Generated by Django 4.2.5 on 2023-10-03 12:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('block', '0007_othertext_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='othertext',
            name='likes',
            field=models.ManyToManyField(related_name='blog_post', to=settings.AUTH_USER_MODEL),
        ),
    ]