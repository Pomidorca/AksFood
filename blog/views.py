from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Category, Email, Contact
from django.core.paginator import Paginator


def index(request):
    # часть кода для пгинации
    recipe_list = Recipe.objects.all()
    paginator = Paginator(recipe_list, 6)  # 6 хреновин на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # Конец части кода, ответственной за пагинацию
    categorys = Category.objects.all()
    count = len(Recipe.objects.all()) - 1
    gallery = Recipe.objects.order_by('image2')[:9]  # 9 изображений для галереи
    if request.method == 'POST':
        if 'email_form' in request.POST:
            email = request.POST.get('email')
            Email.objects.create(email=email)
    if count >= 2:
        product1 = Recipe.objects.all()[count]
        product2 = Recipe.objects.all()[count - 1]
        product3 = Recipe.objects.all()[count - 2]
        return render(request, 'blog/garden-index.html', {'categorys': categorys, 'page_obj': page_obj,
                                                          'product1': product1, 'product2': product2,
                                                          'product3': product3, "gallery": gallery})
    else:
        print('нет рецептов')
    return render(request, 'blog/garden-index.html', {'categorys': categorys, 'page_obj': page_obj, "gallery": gallery})


def category_recipes(request, category_id):
    all_category = Category.objects.all()
    category = get_object_or_404(Category, pk=category_id)
    recipes = Recipe.objects.filter(category=category)
    paginator = Paginator(recipes, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count = len(Recipe.objects.all()) - 1
    gallery = Recipe.objects.order_by('image2', 'category_id')[:9]  # 9 изображений для галереи
    if request.method == 'POST':
        if 'email_form' in request.POST:
            email = request.POST.get('email')
            Email.objects.create(email=email)
    if count >= 2:
        product1 = Recipe.objects.all()[count]
        product2 = Recipe.objects.all()[count - 1]
        product3 = Recipe.objects.all()[count - 2]
        return render(request, 'blog/garden-category.html', {
            'category': category,
            'all_category': all_category,
            'page_obj': page_obj,
            "gallery": gallery,
            'product1': product1, 'product2': product2, 'product3': product3,
        })
    else:
        print('нет рецептов')
        return render(request, 'blog/garden-category.html', {
            'category': category,
            'all_category': all_category,
            'page_obj': page_obj,
            "gallery": gallery,
        })


def add_post(request):
    if request.method == 'POST':
        if 'email_form' in request.POST:
            email = request.POST.get('email')
            Email.objects.create(email=email)
        elif 'contact_form' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            Contact.objects.create(name=name, email=email, phone=phone, subject=subject, message=message)
    return render(request, 'blog/garden-contact.html')


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.views += 1
    recipe.save()
    all_category = Category.objects.all()
    count = len(Recipe.objects.all()) - 1
    gallery = Recipe.objects.order_by('image2')[:9]  # 9 изображений для галереи
    if request.method == 'POST':
        if 'email_form' in request.POST:
            email = request.POST.get('email')
            Email.objects.create(email=email)
    if count >= 2:
        product1 = Recipe.objects.all()[count]
        product2 = Recipe.objects.all()[count - 1]
        product3 = Recipe.objects.all()[count - 2]
        return render(request, 'blog/garden-single.html', {'recipe': recipe, 'all_category': all_category,
                                                           "gallery": gallery,
                                                           'product1': product1, 'product2': product2,
                                                           'product3': product3,
                                                           })
    else:
        return render(request, 'blog/garden-single.html', {'recipe': recipe, 'all_category': all_category,})

def search_view(request):
    query = request.GET.get('q')
    paginator = Paginator(query, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    all_category = Category.objects.all()
    count = len(Recipe.objects.all()) - 1
    if request.method == 'POST':
        if 'email_form' in request.POST:
            email = request.POST.get('email')
            Email.objects.create(email=email)
    results = Recipe.objects.none()
    if query:
        results = Recipe.objects.filter(title__icontains=query) | Recipe.objects.filter(description__icontains=query)
        paginator = Paginator(results, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        gallery = Recipe.objects.order_by('image2')[:9]  # 9 изображений для галереи
    if count >= 2:
        product1 = Recipe.objects.all()[count]
        product2 = Recipe.objects.all()[count - 1]
        product3 = Recipe.objects.all()[count - 2]
        return render(request, 'blog/garden-search.html', {'results': results, 'query': query, 'page_obj': page_obj,
                                                           'all_category': all_category,
                                                           "gallery": gallery,
                                                           'product1': product1, 'product2': product2,
                                                           'product3': product3,})
    else:
        return render(request, 'blog/garden-search.html', {'results': results, 'query': query, 'page_obj': page_obj,
                                                           'all_category': all_category})