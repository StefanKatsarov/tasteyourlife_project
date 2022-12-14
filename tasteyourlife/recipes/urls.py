from django.urls import path

from tasteyourlife.recipes.views import AddRecipeView, BrowseRecipesView, RecipeDetailsView

urlpatterns = [
    path('details/<int:pk>', RecipeDetailsView.as_view(), name='recipe details'),
    path('add/', AddRecipeView.as_view(), name='add recipe'),
    path('all/', BrowseRecipesView.as_view(), name='browse recipes')
]