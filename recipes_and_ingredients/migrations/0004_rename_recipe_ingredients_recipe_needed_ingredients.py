# Generated by Django 3.2.6 on 2021-08-29 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_and_ingredients', '0003_rename_ingredients_recipe_recipe_ingredients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_ingredients',
            new_name='needed_ingredients',
        ),
    ]