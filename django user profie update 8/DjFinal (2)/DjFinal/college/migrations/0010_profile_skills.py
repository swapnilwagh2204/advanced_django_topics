# Generated by Django 3.1.1 on 2020-10-24 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0009_profile_myresume'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.TextField(null=True),
        ),
    ]
