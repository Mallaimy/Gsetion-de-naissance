from django.db.models.query_utils import Q
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from naissanceAPP.forms import EnfantForm, FonctionnaireForm, MereForm, PereForm
from .models import Enfant, Fonctionnaire,Mere, Pere


def mere_list(request):
	meres = Mere.objects.all().order_by('nom')
	return render(request, 'naissances/mere_list.html', {'meres': meres})

def Fonctionnaire_list(request):
	fonctionnaires = Fonctionnaire.objects.all().order_by("nom")
	return render(request, 'naissances/fonctionnaire_list.html', {'fonctionnaires':fonctionnaires})

def pere_list(request):
	peres = Pere.objects.all().order_by('nom')
	return render(request, 'naissances/pere_list.html', {'peres': peres})


def home(request):
	enfants = Enfant.objects.all().order_by('nom')
	return render(request, 'naissances/home.html', {'enfants': enfants})


	

def enfants_list(request):
	enfants = Enfant.objects.all().order_by('nom')
	return render(request, 'naissances/enfants_list.html', {'enfants': enfants})


def ajouter_enfant(request):
    submitted = False
    if request.method == "POST":
        form = EnfantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ajouter_enfant?submitted=True')
    else:
        form = EnfantForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'naissances/ajouter_enfant.html', {
        'form': form,
        'submitted': submitted,
    })



def Editer_enfant(request, enfant_id):
	enfant = Enfant.objects.get(pk=enfant_id)
	form = EnfantForm(request.POST or None, instance=enfant)
	if form.is_valid():
		form.save()
		return redirect('enfants-list')
	return render(request, 'naissances/editer_enfant',{
			'enfant': enfant,
		'form': form,
	}) 



def supprimer_enfant(request, enfant_id):
	enfant = Enfant.objects.get(pk=enfant_id)
	enfant.delete()
	return redirect('enfants-list')

def Montrer_enfant(request, enfant_id):
	enfant = Enfant.objects.get(pk=enfant_id)
	return render(request, 'naissances/montrer_enfant.html', {
		'enfant': enfant,
	})
					
def search_enfant(request):
	if request.method == "GET":
			query = request.GET.get('query')
			if query:
				mutiple_q = Q(Q(nom__icontains=query) | Q(id__icontains=query))
			enfants = Enfant.objects.filter(mutiple_q)
			if enfants:
				return render(request, 'naissances/enfants_list.html', {
					'enfants': enfants
				})
			else:
				print('Not found ...')
				return render(request, 'naissances/not_found.html', {})

#========================================= Mere ========================================================================

def Ajouter_mere(request):
	submitted = False
	if request.method == "POST":
		form = MereForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect ('/ajouter_mere?submitted=True')
	else:
		form = MereForm
		if 'submitted' in request.GET:
			submitted=True
		return render(request, 'naissances/ajouter_mere.html',  {'form': form, 'submitted': submitted,})


def Editer_mere(request, mere_id):
	mere = Mere.objects.get(pk=mere_id)
	form = MereForm(request.POST or None, instance=mere)
	if form.is_valid():
		form.save()
		return redirect('meres-list')
	return render(request, 'naissances/editer_mere.html',{
			'mere': mere,
		'form': form,
	}) 


def supprimer_mere(request, mere_id):
	mere= Mere.objects.get(pk=mere_id)
	mere.delete()
	return redirect('meres-list')

def Montrer_mere(request, mere_id):
	mere = Mere.objects.get(pk=mere_id)
	return render(request, 'naissances/montrer_mere.html', {
		'mere': mere,
	})


def search_mere(request):
	if request.method == "GET":
			query = request.GET.get('query')
			if query:
				mutiple_q = Q(Q(nom__icontains=query) | Q(id__icontains=query))
			mere = Mere.objects.filter(mutiple_q)
			if mere:
				return render(request, 'naissances/mere_list.html', {
					'mere': mere
				})
			else:
				print('Not found ...')
				return render(request, 'naissances/not_found.html', {})

#========================================= Pere ========================================================================

def Ajouter_pere(request):
	submitted = False
	if request.method == "POST":
		form = PereForm (request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect ('/ajouter_pere?submitted=True')
	else:
		form = PereForm
		if 'submitted' in request.GET:
			submitted=True
		return render(request, 'naissances/ajouter_pere.html',  {'form': form, 'submitted': submitted,})



def Editer_pere(request, pere_id):
	pere = Pere.objects.get(pk=pere_id)
	form = PereForm(request.POST or None, instance=pere)
	if form.is_valid():
		form.save()
		return redirect('peres-list')
	return render(request, 'naissances/editer_pere.html',{
			'pere': pere,
		'form': form,
	}) 


def supprimer_pere(request, pere_id):
	pere = Pere.objects.get(pk=pere_id)
	pere.delete()
	return redirect('peres-list')


def Montrer_pere(request, pere_id):
	pere = Pere.objects.get(pk=pere_id)
	return render(request, 'naissances/montrer_pere.html', {
		'pere': pere,
	})


def search_enfant(request):
	if request.method == "GET":
			query = request.GET.get('query')
			if query:
				mutiple_q = Q(Q(nom__icontains=query) | Q(id__icontains=query))
			enfants = Enfant.objects.filter(mutiple_q)
			if enfants:
				return render(request, 'naissances/enfants_list.html', {
					'enfants': enfants
				})
			else:
				print('Not found ...')
				return render(request, 'naissances/not_found.html', {})

#========================================= Pere ========================================================================

def Ajouter_fonctionnaire(request):
	submitted = False
	if request.method == "POST":
		form = FonctionnaireForm (request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect ('/ajouter_fonctionnaire?submitted=True')
	else:
		form = FonctionnaireForm
		if 'submitted' in request.GET:
			submitted=True
		return render(request, 'naissances/ajouter_fonctionnaire.html',  {'form': form, 'submitted': submitted,})


def Editer_fonctionnaire(request, fonctionnaire_id):
	fonctionnaire = Fonctionnaire.objects.get(pk=fonctionnaire_id)
	form = FonctionnaireForm(request.POST or None, instance=fonctionnaire)
	if form.is_valid():
		form.save()
		return redirect('fonctionnaires-list')
	return render(request, 'naissances/editer_fonctionnaires.html',{
			'fonctionnaire': fonctionnaire,
		'form': form,
	}) 


def supprimer_fonctionnaire(request, fonctionnaire_id):
	fonctionnaire = Fonctionnaire.objects.get(pk=fonctionnaire_id)
	fonctionnaire.delete()
	return redirect('fonctionnaires-list')


def Montrer_fonctionnaire(request, fonctionnaire_id):
	fonctionnaire = Fonctionnaire.objects.get(pk=fonctionnaire_id)
	return render(request, 'naissances/montrer_fonctionnaire.html', {
		'fonctionnaire': fonctionnaire,
	})


def search_enfant(request):
	if request.method == "GET":
			query = request.GET.get('query')
			if query:
				mutiple_q = Q(Q(nom__icontains=query) | Q(id__icontains=query))
			enfants = Enfant.objects.filter(mutiple_q)
			if enfants:
				return render(request, 'naissances/enfants_list.html', {
					'enfants': enfants
				})
			else:
				print('Not found ...')
				return render(request, 'naissances/not_found.html', {})
