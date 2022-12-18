from django.contrib import admin

from tasteyourlife.recipes.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'user')
    list_filter = ('user_id',)

