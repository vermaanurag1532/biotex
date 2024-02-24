from django.shortcuts import render, HttpResponseRedirect
from .models import Team, Career

# Create your views here.

def index(request):
    context = {}
    return render(request, 'biotex_app/index.html', context)

def teams(request):
    context = {}
    context['team'] = Team.objects.all()

    return render(request, 'biotex_app/team.html', context)

def career(request):
    context = {}
    context['career'] = Career.objects.all()

    return render(request, 'biotex_app/career.html', context)
