# Generated by Django 3.2.6 on 2021-08-31 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_and_ingredients', '0008_recipe_time_created'),
        ('mealplanner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealplan',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='recipes_and_ingredients.recipe'),
        ),
    ]
