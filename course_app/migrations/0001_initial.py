# Generated by Django 4.1.7 on 2023-05-22 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('instructor', models.CharField(max_length=25)),
                ('duration', models.CharField(max_length=25)),
            ],
        ),
    ]
