# Generated by Django 3.1.5 on 2021-08-01 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210801_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myapp',
            name='image',
            field=models.ImageField(upload_to='my_apps'),
        ),
    ]