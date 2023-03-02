from django import forms
from .models import PredictionModel



class PredictionForm(forms.ModelForm):
    class Meta:
        model = PredictionModel
        fields = ['chambres', 'salles_de_bain', 'm2_habitable', 'm2_Lot', 'etages','vue_sur_leau', 'm2_cave', 'etat', 'm2_above', 'lat', 'long']
    chambres = forms.IntegerField(label='Nombre  de Chambres', widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de Chambres'}))
    salles_de_bain = forms.FloatField(label="Nombre de Salles de Bain", widget = forms.NumberInput(attrs={'class': 'form_check_input'}))
    m2_habitable = forms.IntegerField(label='Espace de vie', widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Espace de Vie'}))
    m2_Lot = forms.IntegerField(label='Surface Terrain', widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Surface Terrrain'}))
    etages = forms.IntegerField(label='Étages', widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Étages'}))
    vue_sur_leau = forms.IntegerField(label='Vue sur la mer', widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Oui = 1, Non = 0'}))
    m2_cave = forms.IntegerField(label='Surface Cave', widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Surface Cave'}))
    etat = forms.IntegerField(label='État', widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Écrire une note entre 1 et 13'}))
    m2_above = forms.IntegerField(label='Surface Habitable', widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Surface Habitable'}))
    lat = forms.FloatField(label='Coordnonnées Latitude', widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Coordnonnées Latitude'}))
    long = forms.FloatField(label='Coordnonnées Longitue', widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Coordnonnées Longitude'}))
    
    
    