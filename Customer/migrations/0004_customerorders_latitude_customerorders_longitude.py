# Generated by Django 4.0.2 on 2022-04-27 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0003_alter_customerorders_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorders',
            name='latitude',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='customerorders',
            name='longitude',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
