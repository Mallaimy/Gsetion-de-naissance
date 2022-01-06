from django.urls import path
from . import views

urlpatterns = [

		path('', views.home, name='home'),
        path('enfants_list/', views.enfants_list, name='enfants-list'),
		path('Ajouter_enfant/', views.Ajouter_enfant, name='Ajouter_enfant'),
		path('editer_enfant/<enfant_id>', views.Editer_enfant, name='editer-enfant'),
		path('supprimer_enfant/<enfant_id>', views.supprimer_enfant, name='supprimer-enfant'),
		path('montrer_enfant/<enfant_id>', views.Montrer_enfant, name='montrer-enfant'),
		path('search_enfant/', views.search_enfant, name='search-enfant'),
		path('peres_list/', views.pere_list, name='peres-list'),


		path('ajouter_mere/', views.Ajouter_mere, name='ajouter_mere'),
		path('editer_mere/', views.Editer_mere, name='editer-mere'),
		path('meres_list/', views.mere_list, name='meres-list'),
		path('fonctionnaire_list/', views.Fonctionnaire_list, name='fonctionnaires-list'),
		

	]