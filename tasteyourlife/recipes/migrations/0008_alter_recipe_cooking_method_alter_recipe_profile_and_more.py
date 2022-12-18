# Generated by Django 4.1.3 on 2022-12-17 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0008_alter_profile_experience_level'),
        ('recipes', '0007_remove_recipe_experience_level_recipe_difficulty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_method',
            field=models.CharField(choices=[('roast', 'Roast'), ('bake', 'Bake'), ('fry', 'Fry'), ('grill', 'Grill'), ('saute', 'Saute'), ('steam', 'Steam'), ('boil', 'Boil'), ('deep_fry', 'Deep fry'), ('other', 'Other')], max_length=8),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
