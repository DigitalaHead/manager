

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomAbilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.TextField(max_length=30, verbose_name='Название таблицы')),
                ('data_table', models.TextField(verbose_name='Таблица данных')),
                ('abilities_chart', models.ImageField(upload_to='images_custom/%Y/%m/%d', verbose_name='График навыков')),
            ],
            options={
                'db_table': 'custom_abilities_table',
            },
        ),
        migrations.CreateModel(
            name='CustomHeadHunterLV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=100, verbose_name='Роль')),
                ('vacancy_to_analyze', models.TextField(max_length=15, verbose_name='Вакансия для анализа')),
            ],
            options={
                'db_table': 'custom_api_table',
            },
        ),
        migrations.CreateModel(
            name='CustomLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_salary_chart', models.ImageField(upload_to='images_custom/%Y/%m/%d', verbose_name='График уровня зарплаты по городам')),
                ('city_vacancy_chart', models.ImageField(upload_to='images_custom/%Y/%m/%d', verbose_name='График доли вакансий по городам')),
                ('data_table', models.TextField(verbose_name='Таблица данных')),
            ],
            options={
                'db_table': 'custom_geography_table',
            },
        ),
        migrations.CreateModel(
            name='CustomMainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_description', models.TextField(blank=True, verbose_name='Описание роли')),
                ('role_photo', models.ImageField(upload_to='images_custom/%Y/%m/%d', verbose_name='Фотография роли')),
            ],
            options={
                'db_table': 'custom_main_table',
            },
        ),
        migrations.CreateModel(
            name='CustomNavigation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.TextField(max_length=25, verbose_name='Роль')),
                ('business_logo', models.ImageField(upload_to='images_custom/%Y/%m/%d', verbose_name='Логотип компании')),
                ('first_item', models.TextField(max_length=25, verbose_name='Первый элемент')),
                ('second_item', models.TextField(max_length=25, verbose_name='Второй элемент')),
                ('third_item', models.TextField(max_length=25, verbose_name='Третий элемент')),
                ('fourth_item', models.TextField(max_length=25, verbose_name='Четвертый элемент')),
                ('fifth_item', models.TextField(max_length=25, verbose_name='Пятый элемент')),
                ('creator', models.TextField(max_length=50, verbose_name='Создатель')),
            ],
            options={
                'db_table': 'custom_navigation_table',
            },
        ),
        migrations.CreateModel(
            name='CustomRelevance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_chart', models.ImageField(upload_to='images_custom/%Y/%m/%d', verbose_name='График уровня зарплаты по годам')),
                ('vacancy_chart', models.ImageField(upload_to='images_custom/%Y/%m/%d', verbose_name='График количества вакансий по годам')),
                ('data_table', models.TextField(verbose_name='Таблица данных')),
            ],
            options={
                'db_table': 'custom_relevance_table',
            },
        ),
    ]
