# Generated by Django 4.2.1 on 2023-05-13 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0009_remove_proj_details_people'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proj_details',
            name='proposer',
        ),
    ]
