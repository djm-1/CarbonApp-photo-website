# Generated by Django 3.0.6 on 2020-12-28 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='static/profile_image'),
        ),
    ]
