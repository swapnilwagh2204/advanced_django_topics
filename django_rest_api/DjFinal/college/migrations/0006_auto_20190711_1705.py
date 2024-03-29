# Generated by Django 2.1.4 on 2019-07-11 11:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0005_auto_20190711_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_no',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='rn',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
