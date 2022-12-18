# Generated by Django 4.1.3 on 2022-12-17 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_profile_experience_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='experience_level',
            field=models.CharField(blank=True, choices=[('amateur', 'Amateur'), ('home_cook', 'Home Cook'), ('expert', 'Expert'), ('professional', 'Professional chef')], max_length=12, null=True),
        ),
    ]
