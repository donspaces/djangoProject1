# Generated by Django 3.2.3 on 2021-09-13 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Module', '0002_auto_20210913_2336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablei',
            old_name='startDate',
            new_name='birth',
        ),
        migrations.RenameField(
            model_name='tablei',
            old_name='amount',
            new_name='height',
        ),
    ]