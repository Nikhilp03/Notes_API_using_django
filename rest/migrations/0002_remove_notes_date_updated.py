# Generated by Django 2.2.7 on 2019-11-21 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='date_updated',
        ),
    ]
