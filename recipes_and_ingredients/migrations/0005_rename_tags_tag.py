# Generated by Django 3.2.6 on 2021-08-30 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_and_ingredients', '0004_rename_recipe_ingredients_recipe_needed_ingredients'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]
