from django.db import models

# Create your models here.

class Fonctionnaire(models.Model):
    nom = models.CharField(' Nom', max_length=30)
    prenom = models.CharField('Prenom', max_length=30)
    genre = models.CharField('Genre', max_length=30)
    telephone =models.CharField('Telephone', max_length=30)
    poste = models.CharField('Poste', max_length=20)

    def __str__(self):
	    return self.nom

class Pere(models.Model):
    nom = models.CharField('Nom', max_length=20)
    prenom = models.CharField('Prenom', max_length=30)
    genre = models.CharField('Genre', max_length=30)
    date_naissance_pere=models.DateField('Date de naissance pere')
    lieu_naissance_pere = models.CharField('Lieu de Naissance pere', max_length=30)
    fonction_pere =models.CharField('Fonction Pere', max_length=30)

    def __str__(self):
	    return self.nom


class Mere(models.Model):
    nom = models.CharField('Nom', max_length=20)
    prenom = models.CharField('Prenom', max_length=30)
    genre = models.CharField('Genre', max_length=30)
    date_naissance_mere=models.DateField('Date de naissance pere')
    lieu_naissance_mere = models.CharField('Lieu de Naissance pere', max_length=30)
    fonction_mere =models.CharField('Fonction Pere', max_length=30)

    def __str__(self):
	    return self.nom



class Enfant(models.Model):
    Arrondissement = models.CharField('Arrondissement', max_length=50)
    nom = models.CharField('Nom', max_length=20)
    prenom = models.CharField('Prenom', max_length=30)
    genre = models.CharField('Genre', max_length=30)
    date_naissance=models.DateField('Date de naissance')
    lieu_naissance= models.CharField('Lieu de Naissance', max_length=30)
    groupe_sanguin = models.CharField("Groupe sanguin", max_length=10)
    pere =models.ForeignKey(Pere, blank=False, null=False, on_delete=models.CASCADE)
    mere =models.ForeignKey(Mere, blank=False, null=False, on_delete=models.CASCADE)
    fonctionnaire = models.ForeignKey(Fonctionnaire, blank=False, null=False, on_delete=models.CASCADE)
    								
    def __str__(self):
	    return self.nom
