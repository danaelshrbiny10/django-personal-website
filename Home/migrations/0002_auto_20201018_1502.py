# Generated by Django 3.1.2 on 2020-10-18 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='home',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
