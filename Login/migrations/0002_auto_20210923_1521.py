# Generated by Django 3.2.3 on 2021-09-23 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pending',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('passwd', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]
