from enum import Enum

from django.contrib.auth import get_user_model
from django.db import models

from tasteyourlife.common.mixins import ChoicesEnumMixin

UserModel = get_user_model()


class Category(ChoicesEnumMixin, Enum):
    stir_fry = 'Stir fry'
    soup = 'Soup'
    dessert = 'Dessert'
    main_dish = 'Main dish'
    salad = 'Salad'
    side_dish = 'Side dish'
    appetizers = 'Appetizers'
    pasta = 'Pasta'
    snacks = 'Snacks'
    other = 'Other'


class Subcategory(ChoicesEnumMixin, Enum):
    gluten_free = 'Gluten free'
    vegan = 'Vegan'
    vegetarian = 'Vegetarian'


class CookingMethod(ChoicesEnumMixin, Enum):
    bake = 'Bake'
    fry = 'Fry'
    grill = 'Grill'


class ExperienceLevel(ChoicesEnumMixin, Enum):
    newbie = 'Newbie'
    regular = 'Regular'
    home_cook = 'Home cook'


class Recipe(models.Model):
    NAME_MAX_LENGTH = 30

    photo = models.ImageField(
        upload_to='recipe_photos/',
        null=False,
        blank=True,
    )
    name = models.CharField(
        max_length=NAME_MAX_LENGTH
    )

    category = models.CharField(
        choices=Category.choices(),
        max_length=Category.max_len()
    )

    subcategory = models.CharField(
        choices=Subcategory.choices(),
        max_length=Subcategory.max_len()

    )

    cooking_method = models.CharField(
        choices=CookingMethod.choices(),
        max_length=CookingMethod.max_len()

    )

    ingredients = models.TextField(

    )

    instructions = models.TextField(

    )

    servings = models.IntegerField(

    )

    preparation_time = models.IntegerField(

    )

    cooking_time = models.IntegerField(

    )

    experience_level = models.CharField(
        choices=ExperienceLevel.choices(),
        max_length=ExperienceLevel.max_len()
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    @property
    def number_of_ingredients(self):
        return len(self.ingredients)
