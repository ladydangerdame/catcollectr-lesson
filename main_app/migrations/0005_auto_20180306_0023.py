# Generated by Django 2.0.2 on 2018-03-06 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_cat_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='likes',
            field=models.IntegerField(),
        ),
    ]