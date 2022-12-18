from django.contrib import admin

from tasteyourlife.common.models import RecipeLike, Article


@admin.register(RecipeLike)
class AdminPhotoLike(admin.ModelAdmin):
    list_display = ('user_id', 'recipe_id')


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ('user_id', 'name')
    ordering = ('user_id', 'name')
    list_filter = ('user_id',)
