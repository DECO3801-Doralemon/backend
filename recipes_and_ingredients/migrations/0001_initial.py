# Generated by Django 3.2.6 on 2021-09-27 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile_feature', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('gtin', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(default='ingredients/test_photo.PNG', upload_to='ingredients')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kg_used', models.FloatField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes_and_ingredients.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('photo', models.ImageField(default='recipes/test_photo.PNG', upload_to='recipes')),
                ('steps', models.TextField(max_length=1000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='profile_feature.customer')),
                ('customers_who_save', models.ManyToManyField(related_name='customers_who_saved', to='profile_feature.Customer')),
                ('recipe_ingredients', models.ManyToManyField(to='recipes_and_ingredients.RecipeIngredient')),
                ('tags', models.ManyToManyField(to='recipes_and_ingredients.Tag')),
            ],
        ),
    ]
