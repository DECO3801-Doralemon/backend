# Generated by Django 3.2.6 on 2021-09-27 09:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityrecipe',
            name='date_time_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='communityrecipe',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]