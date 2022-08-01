# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


# Model Fonction simple par AOB
class Fonction(models.Model):
    fonction_id = models.AutoField(db_column='FONCTION_id', primary_key=True)  # Field name made lowercase.
    fonction_libelle = models.CharField(db_column='FONCTION_libelle', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'fonction'
        
#Model Divion simple  par AOB
class Division(models.Model):
    division_id = models.AutoField(db_column='DIVISION_id', primary_key=True)  # Field name made lowercase.
    division_code = models.IntegerField(db_column='DIVISION_code', unique=True, blank=True, null=True)  # Field name made lowercase.
    division_libelle = models.CharField(db_column='DIVISION_libelle', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'division'
        
# Model Equipement simple par AOB
class Equipement(models.Model):
    equipement_id = models.IntegerField(db_column='EQUIPEMENT_id', primary_key=True)  # Field name made lowercase.
    equipement_libelle = models.CharField(db_column='EQUIPEMENT_libelle', max_length=45, blank=True, null=True)  # Field name made lowercase.
    equipement_categorie = models.CharField(db_column='EQUIPEMENT_categorie', max_length=45, blank=True, null=True)  # Field name made lowercase.
    equipement_caracteristique = models.TextField(db_column='EQUIPEMENT_caracteristique', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'equipement'
        
# Model Fournisseur Simple par YARIE
class Fournisseur(models.Model):
    fournisseur_id = models.AutoField(db_column='FOURNISSEUR_id', primary_key=True)  # Field name made lowercase.
    fournisseur_nom = models.CharField(db_column='FOURNISSEUR_nom', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fournisseur_prenom = models.CharField(db_column='FOURNISSEUR_prenom', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fournisseur_adresse = models.CharField(db_column='FOURNISSEUR_adresse', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fournisseur_telefone = models.CharField(db_column='FOURNISSEUR_telefone', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'fournisseur'
        
# Model MaterielDote Simple par AOB
class MaterielDote(models.Model):
    materiel_dote_id = models.AutoField(db_column='MATERIEL_DOTE_id', primary_key=True)  # Field name made lowercase.
    materiel_dote_numero = models.CharField(db_column='MATERIEL_DOTE_numero', unique=True, max_length=45)  # Field name made lowercase.
    materiel_dote_libelle = models.CharField(db_column='MATERIEL_DOTE_libelle', max_length=45, blank=True, null=True)  # Field name made lowercase.
    materiel_dote_categorie = models.CharField(db_column='MATERIEL_DOTE_categorie', max_length=45, blank=True, null=True)  # Field name made lowercase.
    materiel_dote_caracteristique = models.TextField(db_column='MATERIEL_DOTE_caracteristique', blank=True, null=True)  # Field name made lowercase.
    materiel_dote_dureevie = models.IntegerField(db_column='MATERIEL_DOTE_DureeVie', blank=True, null=True)  # Field name made lowercase.
    materiel_dote_taux = models.CharField(db_column='MATERIEL_DOTE_Taux', max_length=45, blank=True, null=True)  # Field name made lowercase.
    materiel_dote_status = models.IntegerField(db_column='MATERIEL_DOTE_status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'materiel_dote'
        
# Model Personnel par THIERNO
class Personel(User):
    personel_id = models.AutoField(db_column='PERSONEL_id', primary_key=True)  # Field name made lowercase.
    personel_nom = models.CharField(db_column='PERSONEL_nom', max_length=45, blank=True, null=True)  # Field name made lowercase.
    personel_prenom = models.CharField(db_column='PERSONEL_prenom', max_length=75, blank=True, null=True)  # Field name made lowercase.
    personel_matricule = models.CharField(db_column='PERSONEL_Matricule', unique=True, max_length=45)  # Field name made lowercase.
    personel_telefone = models.CharField(db_column='PERSONEL_telefone', max_length=45, blank=True, null=True)  # Field name made lowercase.
    personel_grade = models.CharField(db_column='PERSONEL_grade', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'personel'


# Model Session Cle etrangere Fait par THIERNO
class Section(models.Model):
    section_id = models.AutoField(db_column='SECTION_id', primary_key=True)  # Field name made lowercase.
    division_division = models.ForeignKey(Division, models.DO_NOTHING, db_column='DIVISION_DIVISION_id')  # Field name made lowercase.
    section_code = models.IntegerField(db_column='SECTION_code', unique=True)  # Field name made lowercase.
    section_libelle = models.CharField(db_column='SECTION_libelle', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'section'

# Model Bordereaux Cle etrangere par YARIE
class Bordereaux(models.Model):
    bordereaux_id = models.IntegerField(db_column='BORDEREAUX_id', primary_key=True)  # Field name made lowercase.
    commande_commande = models.ForeignKey('Commande', models.DO_NOTHING, db_column='COMMANDE_COMMANDE_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'bordereaux'
    
# Model Bureau Cle etrangere Fait par AOB
class Bureaux(models.Model):
    bureaux_id = models.AutoField(db_column='BUREAUX_id', primary_key=True)  # Field name made lowercase.
    section_section = models.ForeignKey(Section, models.DO_NOTHING, db_column='SECTION_SECTION_id')  # Field name made lowercase.
    bureaux_code = models.IntegerField(db_column='BUREAUX_code', unique=True)  # Field name made lowercase.
    bureaux_libelle = models.CharField(db_column='BUREAUX_libelle', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'bureaux'
        
# Model Facture Cle etrangere par AOB
class Facture(models.Model):
    facture_id = models.AutoField(db_column='FACTURE_id', primary_key=True)  # Field name made lowercase.
    bordereaux_bordereaux = models.ForeignKey(Bordereaux, models.DO_NOTHING, db_column='BORDEREAUX_BORDEREAUX_id')  # Field name made lowercase.
    facture_copie = models.CharField(db_column='FACTURE_copie', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'facture'

# Model MaterielDemande Cle etrangere Fait par Yarie (Put)
class MaterielDemande(models.Model):
    materiel_demande_id = models.AutoField(db_column='MATERIEL_DEMANDE_id', primary_key=True)  # Field name made lowercase.
    demande_demande = models.ForeignKey('Demande', models.DO_NOTHING, db_column='DEMANDE_DEMANDE_id')  # Field name made lowercase.
    equipement = models.ForeignKey('Equipement',on_delete=models.CASCADE)
    materiel_demande_libelle = models.CharField(db_column='MATERIEL_DEMANDE_libelle', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'materiel_demande'

# Model Depense Cle etrangere par AOB
class Depense(models.Model):
    depense_id = models.IntegerField(db_column='DEPENSE_id', primary_key=True)  # Field name made lowercase.
    depense_libelle = models.CharField(db_column='DEPENSE_libelle', max_length=45, blank=True, null=True)  # Field name made lowercase.
    depense_montant = models.IntegerField(db_column='DEPENSE_montant', blank=True, null=True)  # Field name made lowercase.
    depense_date = models.DateField(db_column='Depense_date', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    bureaux_bureaux = models.ForeignKey(Bureaux, models.DO_NOTHING, db_column='BUREAUX_BUREAUX_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'depense'
        
# Model Demande Cle etrangere par AOB
class Demande(models.Model):
    demande_id = models.AutoField(db_column='DEMANDE_id', primary_key=True)  # Field name made lowercase.
    demande_date = models.DateField(db_column='DEMANDE_date', blank=True, null=True,auto_now_add=True)  # Field name made lowercase.
    demande_personel = models.ForeignKey('Personel', models.DO_NOTHING, db_column='DEMANDE_PERSONEL_id',related_name='expediteur')  # Field name made lowercase.
    demande_personel_destination = models.ForeignKey('Personel', on_delete=models.CASCADE, db_column='DEMANDE_PERSONEL_destination', blank=True, null=True,related_name='destiantion')  # Field name made lowercase.
    demande_lien = models.FileField(upload_to='Demandes',db_column='DEMANDE_lien', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'demande'

# Model Appartenir 2Cle etrangere PAR   AOB
class Appartenir(models.Model):
    appartenir_dte = models.DateField(db_column='APPARTENIR_dte', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    bureaux_bureaux = models.ForeignKey('Bureaux', models.DO_NOTHING, db_column='BUREAUX_BUREAUX_id')  # Field name made lowercase.
    materiel_dote_materiel_dote = models.ForeignKey('MaterielDote', models.DO_NOTHING, db_column='MATERIEL_DOTE_MATERIEL_DOTE_id')  # Field name made lowercase.
    appartenir_status = models.IntegerField(db_column='APPARTENIR_status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'appartenir'

# Model Commande 2Cle etrangere par YARIE
class Commande(models.Model):
    commande_id = models.AutoField(db_column='COMMANDE_id', primary_key=True)  # Field name made lowercase.
    personel_personel = models.ForeignKey('Personel', models.DO_NOTHING, db_column='PERSONEL_PERSONEL_id')  # Field name made lowercase.
    fournisseur_fournisseur = models.ForeignKey('Fournisseur', models.DO_NOTHING, db_column='FOURNISSEUR_FOURNISSEUR_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'commande'

# Model LigneCommande 2cle etrangeres
class LigneCommande(models.Model):
    ligne_commande_id = models.AutoField(db_column='LIGNE_COMMANDE_id', primary_key=True)  # Field name made lowercase.
    equipement_equipement = models.ForeignKey(Equipement, models.DO_NOTHING, db_column='EQUIPEMENT_EQUIPEMENT_id')  # Field name made lowercase.
    commande_commande = models.ForeignKey(Commande, models.DO_NOTHING, db_column='COMMANDE_COMMANDE_id')  # Field name made lowercase.
    ligne_commande_qte = models.IntegerField(db_column='LIGNE_COMMANDE_qte', blank=True, null=True)  # Field name made lowercase.
    ligne_commande_prix_unitaire = models.IntegerField(db_column='LIGNE_COMMANDE_prix_unitaire', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ligne_commande' 

# Model Affecter 3cle etrangeres
class Affecter(models.Model):
    affecter_dte = models.DateField(db_column='AFFECTER_dte', blank=True, null=True,auto_now_add=True)  # Field name made lowercase.
    bureaux_bureaux = models.ForeignKey('Bureaux', models.DO_NOTHING, db_column='BUREAUX_BUREAUX_id')  # Field name made lowercase.
    personel_personel = models.ForeignKey('Personel', models.DO_NOTHING, db_column='PERSONEL_PERSONEL_id')  # Field name made lowercase.
    fonction_fonction = models.ForeignKey('Fonction', models.DO_NOTHING, db_column='FONCTION_FONCTION_id')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'affecter'