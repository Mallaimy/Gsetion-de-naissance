from django.urls import path
from . import views

urlpatterns = [
		path('', views.home, name='home'),
		path('peres_list', views.pere_list, name='peres_list'),
        path('enfants_list', views.enfants_list, name='enfants-list'),
        path('meres_list', views.mere_list, name='meres-list'),
		
		path('Ajouter_enfant', views.Ajouter_enfant, name='Ajouter_enfant'),
		path('Ajouter_mere', views.Ajouter_mere, name='ajouter-mere'),

		path('editer_enfant/<enfant_id>', views.Editer_enfant, name='editer-enfant'),
		path('editer_mere/<mere_id>', views.Editer_mere, name='editer-mere'),

		path('supprimer_enfant/<enfant_id>', views.supprimer_enfant, name='supprimer-enfant'),
		path('supprimer_mere/<mere_id>', views.Supprimer_mere, name='supprimer-mere'),

		path('montrer_enfant/<enfant_id>', views.Montrer_enfant, name='montrer-enfant'),
		path('search_enfant', views.search_enfant, name='search-enfant'),
	]