# Generated by Django 3.2.6 on 2021-08-31 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_and_ingredients', '0009_auto_20210831_1824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='ingredient_gtin',
            new_name='gtin',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='ingredient_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='ingredient_type',
            new_name='type',
        ),
    ]