# Generated by Django 3.2.6 on 2021-09-08 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_and_ingredients', '0010_auto_20210831_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='type',
        ),
    ]