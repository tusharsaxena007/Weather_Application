# Generated by Django 3.0.8 on 2020-08-02 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='image',
            field=models.ImageField(default='', height_field=20, upload_to='images/', width_field=20),
        ),
    ]