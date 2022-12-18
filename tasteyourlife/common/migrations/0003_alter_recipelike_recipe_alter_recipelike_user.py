# Generated by Django 4.1.3 on 2022-12-17 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_remove_recipe_experience_level_recipe_difficulty_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0002_rename_photo_recipelike_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipelike',
            name='recipe',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe'),
        ),
        migrations.AlterField(
            model_name='recipelike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]