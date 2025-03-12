import pandas as pd
import random
from datetime import datetime
import os

def charger_participants(fichier):
    try:
        # Affiche le répertoire de travail actuel où le script cherche le fichier
        print(f"Recherche du fichier dans: {os.getcwd()}")
        
        donnees = pd.read_csv(fichier)
        colonne_nom_prenom = "Nom et prénom"
        return list(donnees[colonne_nom_prenom].dropna())
    except FileNotFoundError:
        print("Erreur: Le fichier CSV n'a pas été trouvé.")
        print("Le fichier doit être placé dans le même répertoire que ce script Python")
        return []
    except Exception as e:
        print(f"Erreur lors du chargement des données: {e}")
        return []

def tirer_au_sort(participants, nombre=2):
    if len(participants) < nombre:
        print(f"Il n'y a pas assez de participants ({len(participants)}) pour tirer {nombre} gagnants.")
        return []
    return random.sample(participants, nombre)

def afficher_resultats(gagnants):
    if not gagnants:
        return
        
    print("\n=== Résultats du tirage au sort ===")
    print(f"Tirage effectué le {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}")
    print("\nLes gagnants sont :")
    for i, gagnant in enumerate(gagnants, 1):
        print(f"{i}. {gagnant}")
    print("\n================================")

# Exécution du programme
# Le fichier reponses.csv doit être dans le même répertoire que ce script
fichier_csv = "reponses1.csv"
participants = charger_participants(fichier_csv)
gagnants = tirer_au_sort(participants)
afficher_resultats(gagnants)