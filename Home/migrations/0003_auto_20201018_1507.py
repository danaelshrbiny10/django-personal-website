# Generated by Django 3.1.2 on 2020-10-18 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20201018_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='description',
            field=models.TextField(max_length=5000),
        ),
    ]