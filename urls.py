from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_d'),
    path('analysis', views.analysis, name='analysis_d'),
    path('patients', views.patients, name='patients_d'),
    path('visits', views.visits, name='visits_d'),
]
