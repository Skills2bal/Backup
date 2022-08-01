from django.urls import path, include

urlpatterns = [
    path('superadmin/', include('App.Administration.SuperAdmin.urls')),
    path('division/',include('App.Administration.Division.urls')),
    path('section/', include('App.Administration.Section.urls')),
    path('fonction/', include('App.Administration.Fonction.urls')), # URL pour l model fonction
    path('bureaux/', include('App.Administration.Bureaux.urls')), #URL pour l model bureaux
    path('equipement/', include('App.Administration.Equipement.urls')), #URL pour le model Equipemet
    path('materieldote/', include('App.Administration.MaterielDote.urls')), #URL pour le model MaterielDote
    path('fournisseur/', include('App.Administration.Fournisseur.urls')), #URL pour le model Fournisseur
    path('materieldemander/', include('App.Administration.MaterielDemander.urls')), #URL pour le model Materiel Demander
    path('personnel/', include('App.Administration.Personel.urls')),
    path('affectation/', include('App.Administration.Affectation.urls')),
    path('depense/', include('App.Administration.Depense.urls')), #URL pour le model Depense
    path('demande/', include('App.Administration.Demande.urls')), #URL pour le model Demande
    path('facture/', include('App.Administration.Facture.urls')), #URL pour le model Facture
    path('appartenir/', include('App.Administration.Appartenir.urls')), #URL pour le model Appartenir
    path('commande/', include('App.Administration.Commande.urls')), #URL pour le model Commande
    path('bordereau/', include('App.Administration.Bordereau.urls')), #URL pour le model Borderaux
    
]
