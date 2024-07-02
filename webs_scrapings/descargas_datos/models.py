from django.db import models


class Scraper (models.Model):
    url = models.URLField(unique=True)
    titulo = models.CharField(max_length=255, blank=True, null=True)
    articulo = models.TextField(blank=True, null=True)
    visitado = models.BooleanField(default=False)
