# Generated by Django 2.1 on 2018-09-01 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='sex',
            field=models.CharField(max_length=5),
        ),
    ]
