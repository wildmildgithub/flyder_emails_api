# Generated by Django 4.1.2 on 2022-10-28 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawledemailaddress',
            name='source',
            field=models.TextField(default=''),
        ),
    ]
