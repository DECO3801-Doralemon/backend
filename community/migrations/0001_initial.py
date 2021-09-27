# Generated by Django 3.2.6 on 2021-09-27 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipes_and_ingredients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('recipe', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recipes_and_ingredients.recipe')),
            ],
        ),
    ]