from django.contrib.auth import get_user_model
from django.db import models

from tasteyourlife.recipes.models import Recipe

UserModel = get_user_model()


class RecipeLike(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        blank=True,
        null=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Article(models.Model):
    NAME_MAX_LENGTH = 25
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=False,
        blank=False
    )

    content = models.TextField(
        null=False,
        blank=False
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    @property
    def content_new_line(self):
        new_line = self.content.split('\n')
        return new_line
