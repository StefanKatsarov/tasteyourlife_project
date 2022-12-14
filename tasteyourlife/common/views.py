from django.views import generic as views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from tasteyourlife.common.utils import get_recipe_url
from tasteyourlife.common.models import RecipeLike
from tasteyourlife.recipes.models import Recipe


def index(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }
    return render(
        request, 'common/index.html', context,
    )


def test_page(request):
    return render(request, 'common/test.html')


@login_required
def like_recipe(request, recipe_id):
    user_liked_recipes = RecipeLike.objects.filter(
        recipe_id=recipe_id,
        user_id=request.user.pk)

    if user_liked_recipes:
        user_liked_recipes.delete()
    else:
        RecipeLike.objects.create(
            recipe_id=recipe_id,
            user_id=request.user.id,
        )

    return redirect(get_recipe_url(request, recipe_id))
