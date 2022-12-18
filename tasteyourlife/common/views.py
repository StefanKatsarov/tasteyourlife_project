from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from tasteyourlife.common.forms import ArticleBaseForm
from tasteyourlife.common.utils import get_recipe_url
from tasteyourlife.common.models import RecipeLike, Article
from tasteyourlife.recipes.models import Recipe

MAX_INDEX_RECIPES_COUNT = 6


def index(request):
    recipes = list(Recipe.objects.order_by('-date_added'))
    recipes = recipes[0:MAX_INDEX_RECIPES_COUNT]

    context = {
        'recipes': recipes,
    }
    return render(
        request, 'common/index.html', context,
    )


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
    context = {
        'user_liked': user_liked_recipes,
    }

    return redirect(get_recipe_url(request, recipe_id))


@login_required()
def add_article(request):
    if request.method == "GET":
        form = ArticleBaseForm()
    else:
        form = ArticleBaseForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            form.save_m2m()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'common/article-create-page.html', context)


class ArticleDetailView(views.DetailView):
    template_name = 'common/article-details-page.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ArticleEditView(views.UpdateView, LoginRequiredMixin):
    template_name = 'common/article-edit-page.html'
    model = Article
    form_class = ArticleBaseForm

    def get_success_url(self):
        return reverse_lazy('article details', kwargs={
            'pk': self.object.pk
        })

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('sign in'))
        current_article = Article.objects.filter(id=kwargs.get('pk')).get()
        if request.user.id != current_article.user_id:
            return redirect(reverse_lazy('url tamper'))
        return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(views.DeleteView, LoginRequiredMixin):
    template_name = 'common/article-delete-page.html'
    model = Article
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('sign in'))
        current_article = Article.objects.filter(id=kwargs.get('pk')).get()
        if request.user.id != current_article.user_id:
            return redirect(reverse_lazy('url tamper'))
        return super().dispatch(request, *args, **kwargs)


def all_articles(request):
    articles = Article.objects.all()

    for article in articles:
        article.content = article.content[0:500]

    context = {
        'articles': articles,
    }
    return render(
        request, 'common/all-articles.html', context,)


def url_tampering(request):
    return render(request, 'common/url-tampering-page.html')
