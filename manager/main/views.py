from datetime import datetime
from django.shortcuts import render
from .models import *


def render_page(http_request, template_name, content):
    context = {'navigation': Navigation.objects.all(), 'content': content}
    return render(http_request, template_name, context)


def render_home(request):
    content = MainPage.objects.all()
    return render_page(request, 'index.html', content)


def render_demand(request):
    content = Relevance.objects.all()
    return render_page(request, 'relevance.html', content)


def render_geography(request):
    content = Location.objects.all()
    return render_page(request, 'geo.html', content)


def render_skills(request):
    content = Abilities.objects.all()
    return render_page(request, 'abilities.html', content)


def render_last_vacancy(request):
    last_vacancies_data = HeadHunterLV.objects.all()

    if last_vacancies_data:
        vacancy_to_analyze = last_vacancies_data[0].vacancy_to_analyze
        hh_api = HeadHunterVacancies(vacancy_to_analyze)
        vacancies = hh_api.get_data_vacancies('2023-12-20', 10)

    context = {'vacs': vacancies, 'last_vacancies_data': last_vacancies_data}
    return render_page(request, 'alv.html', context)
