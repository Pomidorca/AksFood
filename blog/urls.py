from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category_recipes, name='category_recipes'),
    path('addpost', views.add_post, name='add_post'),
]
