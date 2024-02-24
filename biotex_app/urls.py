from django.urls import path

from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('teams', view=views.teams, name='teams'),
    path('career', view=views.career, name='career')
]