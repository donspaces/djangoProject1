# Generated by Django 3.2.3 on 2021-09-14 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Module', '0004_alter_tablei_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablei',
            name='id',
        ),
        migrations.AlterField(
            model_name='tablei',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='name'),
        ),
    ]
