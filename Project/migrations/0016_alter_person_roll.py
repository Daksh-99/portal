# Generated by Django 4.2.1 on 2023-05-14 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0015_alter_person_roll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='roll',
            field=models.IntegerField(),
        ),
    ]
