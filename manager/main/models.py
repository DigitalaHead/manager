from django.db import models


class CustomNavigation(models.Model):
    role_name = models.TextField(blank=False, verbose_name='Роль', max_length=25)
    business_logo = models.ImageField(upload_to='images_custom/%Y/%m/%d', blank=False, verbose_name='Логотип компании')
    first_item = models.TextField(blank=False, verbose_name='Первый элемент', max_length=25)
    second_item = models.TextField(blank=False, verbose_name='Второй элемент', max_length=25)
    third_item = models.TextField(blank=False, verbose_name='Третий элемент', max_length=25)
    fourth_item = models.TextField(blank=False, verbose_name='Четвертый элемент', max_length=25)
    fifth_item = models.TextField(blank=False, verbose_name='Пятый элемент', max_length=25)
    creator = models.TextField(blank=False, verbose_name='Создатель', max_length=50)

    class Meta:
        db_table = 'custom_navigation_table'

    def __str__(self):
        return 'Пользовательская навигация'


class CustomMainPage(models.Model):
    role_description = models.TextField(blank=True, verbose_name='Описание роли')
    role_photo = models.ImageField(upload_to='images_custom/%Y/%m/%d', blank=False, verbose_name='Фотография роли')

    class Meta:
        db_table = 'custom_main_table'

    def __str__(self):
        return 'Пользовательская главная страница'


class CustomRelevance(models.Model):
    salary_chart = models.ImageField(upload_to='images_custom/%Y/%m/%d', blank=False,
                                     verbose_name='График уровня зарплаты по годам')
    vacancy_chart = models.ImageField(upload_to='images_custom/%Y/%m/%d', blank=False,
                                      verbose_name='График количества вакансий по годам')
    data_table = models.TextField(blank=False, verbose_name='Таблица данных')

    class Meta:
        db_table = 'custom_relevance_table'

    def __str__(self):
        return 'Пользовательская востребованность'


class CustomLocation(models.Model):
    city_salary_chart = models.ImageField(upload_to='images_custom/%Y/%m/%d', blank=False,
                                          verbose_name='График уровня зарплаты по городам')
    city_vacancy_chart = models.ImageField(upload_to='images_custom/%Y/%m/%d', blank=False,
                                           verbose_name='График доли вакансий по городам')
    data_table = models.TextField(blank=False, verbose_name='Таблица данных')

    class Meta:
        db_table = 'custom_geography_table'

    def __str__(self):
        return 'Пользовательская география'


class CustomAbilities(models.Model):
    table_name = models.TextField(blank=False, verbose_name='Название таблицы', max_length=30)
    data_table = models.TextField(blank=False, verbose_name='Таблица данных')
    abilities_chart = models.ImageField(upload_to='images_custom/%Y/%m/%d', blank=False, verbose_name='График навыков')

    class Meta:
        db_table = 'custom_abilities_table'

    def __str__(self):
        return 'Пользовательские навыки'


class CustomHeadHunterLV(models.Model):
    role_name = models.CharField(max_length=100, verbose_name='Роль')
    vacancy_to_analyze = models.TextField(blank=False, verbose_name='Вакансия для анализа', max_length=15)

    class Meta:
        db_table = 'custom_api_table'

    def __str__(self):
        return 'Пользовательские последние вакансии'
