# Generated by Django 3.1.1 on 2020-10-24 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0008_profile_myimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='myresume',
            field=models.FileField(null=True, upload_to='doc\\'),
        ),
    ]
