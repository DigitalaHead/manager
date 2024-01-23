from datetime import datetime
from django.shortcuts import render
from .models import *
from .api import HeadHunterVacancies


def render_page(http_request, template_name, content):
    context = {'navigation': CustomNavigation.objects.all(), 'content': content}
    return render(http_request, template_name, context)


def render_home(request):
    content = CustomMainPage.objects.all()
    return render_page(request, 'index.html', content)


def render_demand(request):
    content = CustomRelevance.objects.all()
    return render_page(request, 'relevance.html', content)


def render_geography(request):
    content = CustomLocation.objects.all()
    return render_page(request, 'geo.html', content)


def render_skills(request):
    content = CustomAbilities.objects.all()
    return render_page(request, 'abilities.html', content)


def render_last_vacancy(request):
    last_vacancies_data = CustomHeadHunterLV.objects.all()

    if last_vacancies_data:
        vacancy_to_analyze = last_vacancies_data[0].vacancy_to_analyze
        hh_api = HeadHunterVacancies(vacancy_to_analyze)
        vacancies = hh_api.get_data_vacancies('2024-01-24', 5)
    context = {'vacs': vacancies, 'last_vacancies_data': last_vacancies_data}
    return render_page(request, 'alv.html', context)
