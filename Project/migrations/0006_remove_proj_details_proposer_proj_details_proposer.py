# Generated by Django 4.2.1 on 2023-05-13 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0005_person_rename_details_proj_details_details_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proj_details',
            name='proposer',
        ),
        migrations.AddField(
            model_name='proj_details',
            name='proposer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='proposer', to='Project.person'),
        ),
    ]
