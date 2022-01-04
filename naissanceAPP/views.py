from django.db.models.query_utils import Q
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from naissanceAPP.forms import EnfantForm
from .models import Enfant,Mere, Pere


def mere_list(request):
	meres = Mere.objects.all().order_by('nom')
	return render(request, 'naissances/mere_list.html', {'meres': meres})

def pere_list(request):
	peres = Pere.objects.all().order_by('nom')
	return render(request, 'naissances/pere_list.html', {'peres': peres})


def home(request):
	enfants = Enfant.objects.all().order_by('nom')
	return render(request, 'naissances/home.html', {'enfants': enfants})


	

def enfants_list(request):
	enfants = Enfant.objects.all().order_by('nom')
	return render(request, 'naissances/enfants_list.html', {'enfants': enfants})



def Ajouter_enfant(request):
	submitted = False
	if request.method == "POST":
		form = EnfantForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/Ajouter_enfant?submitted=True')
	else:
		form = EnfantForm
		if 'submitted' in request.GET:
			submitted=True
		
		return render(request, 'naissances/ajouter_enfant',  {'form': form, 'submitted': submitted})



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
					