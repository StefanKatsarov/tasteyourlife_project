# Generated by Django 4.1.3 on 2022-12-11 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_appuser_date_joined_alter_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]
