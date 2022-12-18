from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from tasteyourlife.accounts.models import Profile
from tasteyourlife.common.models import RecipeLike
from tasteyourlife.recipes.forms import RecipeBaseForm
from tasteyourlife.recipes.models import Recipe


@login_required
def add_recipe(request):
    if request.method == "GET":
        form = RecipeBaseForm()
    else:
        form = RecipeBaseForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            print(form.errors.as_data())
            recipe.user = request.user
            recipe.profile = Profile.objects.filter(user_id=request.user.id).get()
            recipe.save()
            form.save_m2m()
            return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'recipe/recipe-add-page.html', context)


class RecipeEditView(views.UpdateView):
    template_name = 'recipe/recipe-edit-page.html'
    model = Recipe
    form_class = RecipeBaseForm

    def get_success_url(self):
        return reverse_lazy('recipe details', kwargs={
            'pk': self.object.pk
        })

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('sign in'))
        current_recipe = Recipe.objects.filter(id=kwargs.get('pk')).get()
        if request.user.id != current_recipe.user_id:
            return redirect(reverse_lazy('url tamper'))
        return super().dispatch(request, *args, **kwargs)


class RecipeDeleteView(views.DeleteView):
    template_name = 'recipe/recipe-delete-page.html'
    model = Recipe
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('sign in'))
        current_recipe = Recipe.objects.filter(id=kwargs.get('pk')).get()
        if request.user.id != current_recipe.user_id:
            return redirect(reverse_lazy('url tamper'))
        return super().dispatch(request, *args, **kwargs)


def listProducts(request):
    PRODUCTS_PER_PAGE = 6
    ordering = request.GET.get('ordering', "")
    search = request.GET.get('search', "")
    category = request.GET.get('category', "")
    subcategory = request.GET.get('subcategory', "")
    cooking_method = request.GET.get('cooking-method', "")
    difficulty = request.GET.get('difficulty', "")

    if search:
        recipe = Recipe.objects.filter(Q(name__icontains=search) | Q(
            ingredients__icontains=search))

    else:
        recipe = Recipe.objects.all()

    if ordering:
        recipe = recipe.order_by(ordering)

    if category:
        recipe = recipe.filter(category=category)

    if subcategory:
        recipe = recipe.filter(subcategory=subcategory)

    if cooking_method:
        recipe = recipe.filter(cooking_method=cooking_method)

    if difficulty:
        recipe = recipe.filter(difficulty=difficulty)

    # Pagination
    page = request.GET.get('page', 1)
    recipe_paginator = Paginator(recipe, PRODUCTS_PER_PAGE)
    try:
        recipe = recipe_paginator.page(page)
    except EmptyPage:
        recipe = recipe_paginator.page(recipe_paginator.num_pages)
    except:
        recipe = recipe_paginator.page(PRODUCTS_PER_PAGE)
    return render(request, "recipe/recipe-browse-page.html",
                  {"recipes": recipe, 'page_obj': recipe, 'is_paginated': True, 'paginator': recipe_paginator})


class RecipeDetailsView(views.DetailView):
    model = Recipe
    template_name = 'recipe/recipe-details-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_likes = len(RecipeLike.objects.filter(recipe_id=self.object.pk))
        user_liked_current_recipe = RecipeLike.objects.filter(user_id=self.request.user.id, recipe_id=self.object.pk)
        context['recipe_likes'] = recipe_likes
        context['liked_by_user'] = user_liked_current_recipe

        return context

