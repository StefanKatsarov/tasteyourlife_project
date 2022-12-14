from django.contrib import admin

from tasteyourlife.common.models import RecipeLike


@admin.register(RecipeLike)
class AdminPhotoLike(admin.ModelAdmin):
    pass
