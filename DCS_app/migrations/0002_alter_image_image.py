# Generated by Django 4.1.1 on 2023-02-07 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DCS_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]