# Generated by Django 4.1.7 on 2023-06-27 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ead', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eaduser',
            name='mobile',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
