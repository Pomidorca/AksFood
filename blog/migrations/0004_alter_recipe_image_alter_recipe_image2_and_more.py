# Generated by Django 5.0.7 on 2024-07-15 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_recipe_category_alter_recipe_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to='images', verbose_name='Фотография 1'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image2',
            field=models.ImageField(null=True, upload_to='images', verbose_name='Фотография 2'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/', verbose_name='Видео'),
        ),
    ]
