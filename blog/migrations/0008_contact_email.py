# Generated by Django 5.0.7 on 2024-07-16 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_recipe_additional_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Почта')),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='Телефон')),
                ('subject', models.CharField(max_length=200, null=True, verbose_name='Тема')),
                ('message', models.TextField(null=True, verbose_name='Сообщение')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Почта для рассылки')),
            ],
        ),
    ]
