from django.contrib import admin

from .models import Category, Recipe, Email, Contact
# Register your models here.
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Email)
admin.site.register(Contact)
