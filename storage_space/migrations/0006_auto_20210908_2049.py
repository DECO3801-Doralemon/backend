# Generated by Django 3.2.6 on 2021-09-08 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_and_ingredients', '0012_rename_weight_used_recipeingredient_kg_used'),
        ('profile_feature', '0008_alter_customer_photo'),
        ('storage_space', '0005_auto_20210908_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoredIngredientInFreezer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiry_date', models.DateField()),
                ('kg', models.FloatField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_feature.customer')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes_and_ingredients.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='StoredIngredientInFridge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiry_date', models.DateField()),
                ('kg', models.FloatField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_feature.customer')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes_and_ingredients.ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='StoredIngredientInPantry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiry_date', models.DateField()),
                ('kg', models.FloatField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_feature.customer')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes_and_ingredients.ingredient')),
            ],
        ),
        migrations.DeleteModel(
            name='StoredIngredient',
        ),
    ]