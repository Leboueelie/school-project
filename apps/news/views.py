from django.shortcuts import get_object_or_404, render

from .models import Actualite


def liste_actualites(request):
    actualites = Actualite.objects.all()
    return render(request, "news/liste.html", {"actualites": actualites})


def detail_actualite(request, pk):
    actualite = get_object_or_404(Actualite, pk=pk)
    return render(request, "news/detail.html", {"actualite": actualite})
