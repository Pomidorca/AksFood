from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Category


def index(request):
    recipes = Recipe.objects.all()
    category = Category.objects.all()
    count = len(Recipe.objects.all()) - 1
    if count >= 2:
        product1 = Recipe.objects.all()[count]
        product2 = Recipe.objects.all()[count - 1]
        product3 = Recipe.objects.all()[count - 2]
        return render(request, 'blog/garden-index.html', {'category': category, 'recipes': recipes,
                                                          'product1': product1, 'product2': product2,
                                                          'product3': product3})
    else:
        print('нет рецептов')
    return render(request, 'blog/garden-index.html', {'category': category, 'recipes': recipes})
