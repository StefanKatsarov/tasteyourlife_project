# Generated by Django 4.1.3 on 2022-12-11 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(blank=True, upload_to='pet_photos/'),
        ),
    ]