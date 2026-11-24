from django import forms

from .models import Musica


class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ['titulo', 'artista', 'album', 'genero', 'ano']
        labels = {
            'titulo': 'Título',
            'artista': 'Artista',
            'album': 'Álbum (opcional)',
            'genero': 'Gênero',
            'ano': 'Ano de lançamento (opcional)',
        }