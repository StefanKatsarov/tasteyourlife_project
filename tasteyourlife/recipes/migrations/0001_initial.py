# Generated by Django 4.1.3 on 2022-12-04 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('stir_fry', 'Stir fry'), ('soup', 'Soup'), ('dessert', 'Dessert'), ('main_dish', 'Main dish'), ('salad', 'Salad'), ('side_dish', 'Side dish'), ('appetizers', 'Appetizers'), ('pasta', 'Pasta'), ('snacks', 'Snacks'), ('other', 'Other')], max_length=10)),
                ('subcategory', models.CharField(choices=[('gluten_free', 'Gluten free'), ('vegan', 'Vegan'), ('vegetarian', 'Vegetarian')], max_length=11)),
                ('cooking_method', models.CharField(choices=[('bake', 'Bake'), ('fry', 'Fry'), ('grill', 'Grill')], max_length=5)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('servings', models.IntegerField()),
                ('preparation_time', models.IntegerField()),
                ('cooking_time', models.IntegerField()),
                ('experience_level', models.CharField(choices=[('newbie', 'Newbie'), ('regular', 'Regular'), ('home_cook', 'Home cook')], max_length=9)),
            ],
        ),
    ]
