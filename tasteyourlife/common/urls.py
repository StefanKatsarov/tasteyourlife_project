from django.urls import path, include

from tasteyourlife.common.views import index, like_recipe, ArticleEditView, ArticleDetailView, \
    ArticleDeleteView, add_article, all_articles, url_tampering

urlpatterns = [
    path('', index, name='index'),
    path('like/<int:recipe_id>/', like_recipe, name='like recipe'),
    path('article/', include([
        path('<int:pk>/', ArticleDetailView.as_view(), name='article details'),
        path('add/', add_article, name='article create'),
        path('edit/<int:pk>/', ArticleEditView.as_view(), name='article edit'),
        path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='article delete'),
        path('all/', all_articles, name='all articles'),
    ])),
    path('url-tampering-error/', url_tampering, name='url tamper')
]
