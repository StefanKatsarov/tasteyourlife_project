from django.urls import path

from tasteyourlife.common.views import test_page, index, like_recipe

urlpatterns = [
    path('', index, name='index'),
    path('test/', test_page, name='test'),
    path('like/<int:recipe_id>/', like_recipe, name='like recipe'),
]
