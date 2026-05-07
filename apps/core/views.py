from django.shortcuts import render

from apps.news.models import Actualite


def home(request):
    recentes = Actualite.objects.all()[:3]  # 3 dernières pour l'accueil
    return render(request, "core/home.html", {"recentes": recentes})


def apropos(request):
    return render(request, "core/apropos.html")
