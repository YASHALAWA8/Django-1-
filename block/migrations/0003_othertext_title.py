# Generated by Django 4.2.3 on 2023-08-07 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0002_othertext_remove_article_sumary'),
    ]

    operations = [
        migrations.AddField(
            model_name='othertext',
            name='title',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]
