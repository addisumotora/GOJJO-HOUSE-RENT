# Generated by Django 3.2.13 on 2022-04-29 19:28

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='posts/default.jpg', upload_to=posts.models.upload_to, verbose_name='Image'),
        ),
    ]
