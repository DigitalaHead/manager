from django.urls import path
from .views import *

urlpatterns = [
    path('', render_home, name='index'),
    path('relevance', demand_page, name='relevance'),
    path('geography', geography_page, name='geo'),
    path('abilities', skills_page, name='abilities'),
    path('api_last_vacancy', last_vacancy_page, name='alv'),
]
