# Generated by Django 3.2.6 on 2021-08-31 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_feature', '0007_alter_customer_photo'),
        ('storage_space', '0002_auto_20210831_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='storedingredient',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profile_feature.customer'),
            preserve_default=False,
        ),
    ]