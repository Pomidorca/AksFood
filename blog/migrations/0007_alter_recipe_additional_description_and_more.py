# Generated by Django 5.0.7 on 2024-07-16 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_recipe_additional_description_recipe_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='additional_description',
            field=models.TextField(blank=True, null=True, verbose_name='Дополнительное описание'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='Счётчик просмотров'),
        ),
    ]