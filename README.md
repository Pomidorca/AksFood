AksFood Blog


AksFood Blog - это кулинарный блог, разработанный на Django, поддерживающий создание, редактирование и удаление рецептов с добавлением фотографий и видео. Также имеется возможность фильтрации рецептов по категориям и поиска по ключевым словам. В проекте реализована пагинация для удобного просмотра большого количества рецептов.
Установка и настройка
Предварительные требования

    Python 3.7+
    Django 3.2+
    Виртуальное окружение (рекомендуется)

Инструкции по установке

    Клонируйте репозиторий:

    git clone https://github.com/ваш-логин/aksfood-blog.git
    cd aksfood-blog

Создайте и активируйте виртуальное окружение:

    python -m venv env
    source env/bin/activate  # Для Windows используйте `env\Scripts\activate`

Выполните миграции для настройки базы данных:

    python manage.py migrate

Создайте суперпользователя для доступа к административной панели:

    python manage.py createsuperuser

Запустите сервер разработки:

    python manage.py runserver

Теперь вы можете открыть браузер и перейти по адресу http://127.0.0.1:8000/, чтобы увидеть работающий сайт.
Примеры использования
Создание рецепта

    Перейдите на страницу администрирования: http://127.0.0.1:8000/admin/
    Войдите под учетной записью суперпользователя.
    В разделе "Recipes" выберите "Add".
    Заполните форму, добавив заголовок, описание, фото, видео и выбрав категорию.
    Нажмите "Save".

Поиск рецептов

    На главной странице введите ключевые слова в поле поиска.
    Нажмите "Search".
    Результаты поиска будут отображены с возможностью пагинации.

Фильтрация по категориям

    На главной странице выберите интересующую категорию из списка категорий.
    Список рецептов автоматически обновится, показывая только те, которые относятся к выбранной категории.

Основные функции

    Создание, редактирование и удаление рецептов: Возможность добавлять новые рецепты, редактировать существующие и удалять ненужные.
    Добавление медиа-контента: Поддержка добавления фотографий и видео к рецептам.
    Фильтрация по категориям: Просмотр рецептов, относящихся к определенным категориям.
    Поиск рецептов: Поиск рецептов по ключевым словам в заголовках и описаниях.
    Пагинация: Удобная навигация по страницам с рецептами.

Используемые технологии и библиотеки

    Django: Веб-фреймворк для разработки проекта.
    SQLite: Встроенная база данных для хранения данных.
    Bootstrap: CSS-фреймворк для стилизации интерфейса.
    HTML/CSS/JavaScript: Стандартные веб-технологии для создания пользовательского интерфейса.

Контакты

Если у вас есть вопросы или предложения по улучшению проекта, пожалуйста, свяжитесь со мной по электронной почте: roma.aksenov.04@list.ru

Этот файл README предоставляет общее представление о проекте AksFood Blog, инструкции по установке и настройке, примеры использования, описание основных функций и список используемых технологий и библиотек.
