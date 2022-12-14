from django.contrib.auth import get_user_model
from django.db import models

from tasteyourlife.recipes.models import Recipe

UserModel = get_user_model()


class RecipeLike(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.RESTRICT,
        blank=True,
        null=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )
