# Generated by Django 2.1.4 on 2019-07-11 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0008_profile_myimg'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='myresume',
            field=models.FileField(blank=True, null=True, upload_to='docs//'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='myimg',
            field=models.ImageField(null=True, upload_to='images//'),
        ),
    ]
