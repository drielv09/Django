from django.db import models

class Musica(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    album = models.CharField(max_length=100, blank=True)
    genero = models.CharField(max_length=50)
    ano = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['artista', 'titulo'] #ordem alfabética por artista 

    def __str__(self):
        return f"{self.titulo} - {self.artista}"