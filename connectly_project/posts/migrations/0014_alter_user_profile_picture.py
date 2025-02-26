# Generated by Django 5.1.4 on 2025-02-26 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_pictures/default.jpg', upload_to='profile_pictures/'),
        ),
    ]
