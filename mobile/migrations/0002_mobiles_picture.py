# Generated by Django 4.2.6 on 2023-11-19 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobiles',
            name='picture',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
