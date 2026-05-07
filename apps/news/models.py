from django.db import models


class Actualite(models.Model):
    titre = models.CharField("Titre de l'actualité", max_length=200)
    contenu = models.TextField("Contenu détaillé")
    image = models.ImageField(
        "Image d'illustration", upload_to="actualites/", blank=True, null=True
    )
    date_publication = models.DateTimeField("Date de publication", auto_now_add=True)

    class Meta:
        verbose_name = "Actualité"
        verbose_name_plural = "Actualités"
        ordering = ["-date_publication"]  # Les plus récentes en premier

    def __str__(self):
        return self.titre
