# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 08:44:26 2021

@author: anais
"""

import sqlite3

connexion = sqlite3.connect('hotellerie.db')
curseur = connexion.cursor()

def affiche_hotel():
    nomVille=str(input("Saisir nom de ville à rechercher "))
    
    ligne = curseur.fetchall()
    requete= "SELECT * FROM hotel WHERE ville='" +nomVille+"' "
    
    for ligne in curseur.execute(requete):
     print (ligne)

def ajout_client():
    nom=str(input("Saisir le nom à entrer "))
    prenom=str(input("Saisir le prénom à entrer "))
    
    requeteVNP= "SELECT * FROM client WHERE nom='"+nom+"' AND prenom='"+prenom+"'"
    curseur.execute(requeteVNP)  
    existe = curseur.fetchone()

    if existe is None:
        print("Ajout de l utilisateur dans la BDD")
        requeteNP= "INSERT INTO client (nom, prenom) VALUES ('"+nom+"','"+prenom+"')"
        #OperationalError: database is locked impossible d'exécuter la requête
        curseur.execute(requeteNP)        
    else:
        print("Ce client existe déjà, veuillez réessayez")
        
def bien_arrivee():
    numclient=int(input("Saisr le numéro de client "))
    numhotel=int(input("Saisie le numéro d'hotel "))
    date_arrivee=str(input("Saisir la date d'arrivée au format AAAA-MM-JJ "))
    requeteBA= "SELECT * FROM reservation WHERE numclient='" +numclient+"' AND numhotel='"+numhotel+"' AND datearrivee='"+date_arrivee+"'"
    curseur.execute(requeteBA)  
    existe = curseur.fetchone()
    
    if existe is None:
        print("Réservation trouvée. Suppression de votre réservation de la base de données.")
        requeteDEL=("DELETE FROM reservation WHERE numclient='" +numclient+"' AND numhotel='"+numhotel+"' AND datearrivee='"+date_arrivee+"'")
        curseur.execute(requeteDEL)
    else:
        print("Aucune réservation trouvée. Veuillez vérifier votre saisie.")

bien_arrivee()
connexion.commit()
connexion.close()
