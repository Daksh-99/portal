# Generated by Django 4.2.1 on 2023-05-10 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proj_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Details', models.TextField()),
                ('Proposer', models.CharField(max_length=255)),
            ],
        ),
    ]
