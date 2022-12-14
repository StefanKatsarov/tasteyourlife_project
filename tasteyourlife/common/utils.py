def get_recipe_url(request, recipe_id):
    return request.META['HTTP_REFERER'] + f'#recipe-{recipe_id}'
