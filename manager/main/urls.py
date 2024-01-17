from django.urls import path
from .views import *

urlpatterns = [
    path('', render_home, name='index'),
    path('relevance', render_demand, name='relevance'),
    path('geography', render_geography, name='geo'),
    path('abilities', render_skills, name='abilities'),
    path('api_last_vacancy', render_last_vacancy, name='alv'),
]
