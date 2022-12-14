from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from tasteyourlife.recipes.forms import RecipeBaseForm
from tasteyourlife.recipes.models import Recipe


class AddRecipeView(views.CreateView):
    required_css_class = 'full-width'
    template_name = 'recipe/add-recipe-page.html'
    form_class = RecipeBaseForm
    success_url = reverse_lazy('index')


class BrowseRecipesView(views.ListView):
    template_name = 'recipe/browse-recipes-page.html'
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        recipes = self.object_list

        context['all_recipes'] = recipes

        return context


class RecipeDetailsView(views.DetailView):
    model = Recipe
    template_name = 'recipe/details-recipe-page.html'


def recipe_view(request, pk):
    return render(request, 'recipe/details-recipe-page.html')
