from django.urls import path
from . import views

urlpatterns = [

		path('', views.home, name='home'),
        path('enfants_list/', views.enfants_list, name='enfants-list'),
		path('ajouter_enfant/', views.ajouter_enfant, name='ajouter_enfant'),
		path('editer_enfant/<enfant_id>', views.Editer_enfant, name='editer-enfant'),
		path('supprimer_enfant/<enfant_id>', views.supprimer_enfant, name='supprimer-enfant'),
		path('montrer_enfant/<enfant_id>', views.Montrer_enfant, name='montrer-enfant'),
		path('search_enfant/', views.search_enfant, name='search-enfant'),
		path('meres_list/', views.mere_list, name='meres-list'),
		path('peres_list/', views.pere_list, name='peres-list'),
		path('fonctionnaire_list/', views.Fonctionnaire_list, name='fonctionnaires-list'),



		path('editer_mere/<mere_id>', views.Editer_mere, name='editer-mere'),
		path('meres_list/', views.mere_list, name='meres-list'),
		path('ajouter_mere/', views.Ajouter_mere, name='ajouter_mere'),
		path('supprimer_mere/<mere_id>', views.supprimer_mere, name='supprimer-mere'),
		path('montrer_mere/<mere_id>', views.Montrer_mere, name='montrer-mere'),
		path('search_mere/', views.search_mere, name='search-mere'),


		path('peres_list/', views.pere_list, name='peres-list'),
		path('ajouter_pere/', views.Ajouter_pere, name='ajouter_pere'),
		path('editer_pere/<pere_id>', views.Editer_pere, name='editer-pere'),
		path('supprimer_pere/<pere_id>', views.supprimer_pere, name='supprimer-pere'),
		path('montrer_pere/<pere_id>', views.Montrer_pere, name='montrer-pere'),
		
		
		
		path('fonctionnaire_list/', views.Fonctionnaire_list, name='fonctionnaires-list'),
		path('ajouter_fonctionnaire/', views.Ajouter_fonctionnaire, name='ajouter-fonctionnaire'),
		path('editer_fonctionnaire/<fonctionnaire_id>', views.Editer_fonctionnaire, name='editer-fonctionnaire'),
		path('supprimer_fonctionnaire/<fonctionnaire_id>', views.supprimer_fonctionnaire, name='supprimer-fonctionnaire'),
		path('montrer_fonctionnaire/<fonctionnaire_id>', views.Montrer_fonctionnaire, name='montrer-fonctionnaire'),

	]