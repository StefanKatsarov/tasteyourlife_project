from enum import Enum

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from tasteyourlife.accounts.models import Profile
from tasteyourlife.common.mixins import ChoicesEnumMixin

UserModel = get_user_model()


def make_into_hours(self, time):
    hours = time // 60
    if time >= 60:
        return "%02d:%02d" % (hours, time % 60)


class Category(ChoicesEnumMixin, Enum):
    beef_recipes = 'Beef recipes'
    chicken_recipes = 'Chicken recipes'
    pork_recipes = 'Pork recipes'
    lamb_recipes = 'Lamb recipes'
    stir_fry = 'Stir fry'
    sushi = 'Sushi'
    soup = 'Soup'
    dessert = 'Dessert'
    salad = 'Salad'
    appetizers = 'Appetizers'
    pasta = 'Pasta'
    snacks = 'Snacks'
    sea_food = 'Sea food'
    sandwiches = 'Sandwiches'
    pizza = 'Pizza'
    other = 'Other'


class Subcategory(ChoicesEnumMixin, Enum):
    none = 'None'
    vegan = 'Vegan'
    vegetarian = 'Vegetarian'
    dairy_free = ' Dairy-free'
    gluten_free = 'Gluten-free'


class CookingMethod(ChoicesEnumMixin, Enum):
    roast = 'Roast'
    bake = 'Bake'
    fry = 'Fry'
    grill = 'Grill'
    saute = 'Saute'
    steam = 'Steam'
    boil = 'Boil'
    deep_fry = 'Deep fry'
    other = 'Other'


class Difficulty(ChoicesEnumMixin, Enum):
    easy = 'Easy'
    normal = 'Normal'
    hard = 'Hard'
    expert = 'Expert'


class Recipe(models.Model):
    NAME_MAX_LENGTH = 40

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

    difficulty = models.CharField(
        choices=Difficulty.choices(),
        max_length=Difficulty.max_len()
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    date_added = models.DateTimeField(
        default=timezone.now,
    )

    @property
    def number_of_ingredients(self):
        return len(self.ingredients_list)

    @property
    def total_time_in_minutes(self):
        total_time_in_minutes = self.cooking_time + self.preparation_time
        return total_time_in_minutes

    @property
    def total_time_above_hour(self):
        total_time_in_minutes = self.cooking_time + self.preparation_time
        hours = total_time_in_minutes // 60
        if total_time_in_minutes >= 60:
            return "%02d:%02d" % (hours, total_time_in_minutes % 60)

    @property
    def ingredients_list(self):
        ing_list = self.ingredients.split('\n')
        return ing_list

    @property
    def instructions_newline(self):
        new_line = self.instructions.split('\n')
        return new_line

