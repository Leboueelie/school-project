from django.urls import path

from . import views

urlpatterns = [
    path("", views.liste_actualites, name="liste_actualites"),
    path("<int:pk>/", views.detail_actualite, name="detail_actualite"),
]
