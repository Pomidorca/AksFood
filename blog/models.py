from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def recipe_count(self):
        return self.recipe_set.count()

class Recipe(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    ingredients = models.TextField(verbose_name='Ингридиенты')
    instructions = models.TextField(verbose_name='Инструкция')
    image = models.ImageField(null=True, upload_to='images', verbose_name='Фотография 1')
    image2 = models.ImageField(null=True, upload_to='images', verbose_name='Фотография 2')
    video = models.FileField(upload_to='videos/', null=True, blank=True, verbose_name='Видео')
    created_at = models.DateField(default=timezone.now, verbose_name='Дата создания')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, verbose_name='Категория')

    def __str__(self):
        return f"{self.title}, {self.created_at}"
