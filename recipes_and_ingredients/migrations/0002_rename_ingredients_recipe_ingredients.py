# Generated by Django 3.2.6 on 2021-08-29 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_and_ingredients', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='Ingredients',
            new_name='Ingredients',
        ),
    ]
