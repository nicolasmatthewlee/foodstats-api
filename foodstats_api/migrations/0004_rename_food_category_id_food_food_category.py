# Generated by Django 4.1 on 2023-09-18 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodstats_api', '0003_foodcategory_alter_food_food_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='food_category_id',
            new_name='food_category',
        ),
    ]