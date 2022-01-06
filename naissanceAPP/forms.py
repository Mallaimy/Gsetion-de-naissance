from django import forms
from naissanceAPP.models import Enfant, Mere
from django.forms import ModelForm


class EnfantForm(ModelForm):
    class Meta:
        model = Enfant
        fields = ( 
                       
                        "nom",
                        "prenom",
                        "genre",
                        "date_naissance",
                        "lieu_naissance",
                        "pere",
                        "mere",
                        "fonctionnaire"
                )

        labels = {
                    "nom":"",
                    "prenom":"",
                    "genre":"",
                    "date_naissance":"",
                    "lieu_naissance":"",
                    "pere":"",
                    "mere":"",
                    "fonctionnaire":""
    	        }

        widgets = {
    		'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom',}),  
    		'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenom',}), 
    		'genre': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Genre',}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date naissance',}),
            'lieu_naissance': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lieu de naissance',}), 
    		'mere': forms.Select(attrs={'class': 'form-control', 'placeholder': 'nom du Pere',}),  
    		'pere': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Nom de la mere',}), 
    		'fonctionnaire': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Non du Fonctionnaire',}), 
    		
            
    	}


class MereForm(ModelForm):
    class Meta:
        model = Mere
        fields = ( 
                       
                        "nom",
                        "prenom",
                        "genre",
                        "date_naissance_mere",
                        "lieu_naissance_mere",
                        "fonction_mere"
                )

        labels = {
                    "nom":"",
                    "prenom":"",
                    "genre":"",
                    "date_naissance_mere":"",
                    "lieu_naissance_mere":"",
                    "fonction_mere":""
    	        }

        widgets = {
    		'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom',}),  
    		'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenom',}), 
    		'genre': forms.TextInput(attrs={'class': 'form-select', 'placeholder': 'Genre',}),
            'date_naissance_mere': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date naissance',}),
            'lieu_naissance_mere': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lieu de naissance',}),
    		'fonction_mere': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Fonction de la mere',}),    
    	}



