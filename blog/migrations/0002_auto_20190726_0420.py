# Generated by Django 2.2.3 on 2019-07-25 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='head_image',
            field=models.ImageField(default='default1.jpg', upload_to='blog_pic'),
        ),
    ]
