# Generated by Django 4.2.1 on 2023-05-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0013_proj_details_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proj_details',
            name='people',
            field=models.ManyToManyField(to='Project.person'),
        ),
        migrations.AlterField(
            model_name='proj_details',
            name='proposer',
            field=models.CharField(max_length=40),
        ),
    ]
