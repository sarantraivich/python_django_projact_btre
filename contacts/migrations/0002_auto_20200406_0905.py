# Generated by Django 3.0.4 on 2020-04-06 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contacts',
            new_name='contact',
        ),
    ]
