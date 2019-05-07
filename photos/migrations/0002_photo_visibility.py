# Generated by Django 2.2.1 on 2019-05-07 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='visibility',
            field=models.CharField(choices=[['PUB', 'Public'], ['PRI', 'Private']], default='PUB', max_length=3),
        ),
    ]
