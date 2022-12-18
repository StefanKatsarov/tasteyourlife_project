from django.urls import path
from tasteyourlife.recipes.views import RecipeDetailsView, add_recipe, listProducts, RecipeEditView, RecipeDeleteView

urlpatterns = [
    path('details/<int:pk>', RecipeDetailsView.as_view(), name='recipe details'),
    path('edit/<int:pk>', RecipeEditView.as_view(), name='edit recipe'),
    path('delete/<int:pk>', RecipeDeleteView.as_view(), name='delete recipe'),
    path('add/', add_recipe, name='add recipe'),
    path('all/', listProducts, name='browse recipes'),
]