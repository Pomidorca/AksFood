# Generated by Django 5.0.7 on 2024-07-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_recipe_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='additional_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
