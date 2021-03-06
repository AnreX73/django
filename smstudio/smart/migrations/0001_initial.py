# Generated by Django 3.2.13 on 2022-06-08 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категорию услуг',
                'verbose_name_plural': 'Категории услуг',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='котакты и навигация')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('image', models.ImageField(blank=True, upload_to='images', verbose_name='Изображение')),
                ('annotations1', models.TextField(blank=True, verbose_name='первое значение')),
                ('annotations2', models.TextField(blank=True, verbose_name='второе значение или ссылка на карту')),
            ],
            options={
                'verbose_name': 'контакты и навигация',
                'verbose_name_plural': 'Контакты и навигация',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Новость')),
                ('content', models.TextField(blank=True, verbose_name='Текст новости')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новость',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('menu_image', models.ImageField(upload_to='images', verbose_name='Изображение в меню')),
                ('page_image', models.ImageField(upload_to='images', verbose_name='Изображение на странице')),
                ('annotation', models.TextField(blank=True, verbose_name='Рекламное описание ')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='smart.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Фотоуслуги и сувениры',
                'verbose_name_plural': 'Фотоуслуги и сувениры',
                'ordering': ['time_create', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Цены')),
                ('extraLink', models.CharField(blank=True, max_length=100, verbose_name='Ссылка на дополнительную информацию(если есть)')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='smart.services', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Цены',
                'verbose_name_plural': 'Цены',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Подробное описание')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('extraContent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='smart.prices', verbose_name='Дополнительня информация о...')),
            ],
            options={
                'verbose_name': 'Дополнительня информация',
                'verbose_name_plural': 'Дополнительня информация',
                'ordering': ['id'],
            },
        ),
    ]
