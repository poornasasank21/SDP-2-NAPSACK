# Generated by Django 4.0.2 on 2022-05-12 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0009_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerusers',
            name='image',
            field=models.ImageField(default='customer_images/default_profile_img.png', upload_to='customer_images'),
        ),
    ]
