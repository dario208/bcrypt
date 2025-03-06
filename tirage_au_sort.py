import pandas as pd
import random


fichier_csv = "reponses.csv"  
donnees = pd.read_csv(fichier_csv)

# Supposons que la colonne s'appelle "Nom et Prénom"
colonne_nom_prenom = "Nom et prénom"  # Remplace par le nom exact de ta colonne
noms_prenoms = donnees[colonne_nom_prenom].dropna()  # Supprime les lignes vides

# Convertir en liste de participants
participants = list(noms_prenoms)

# Vérifier s'il y a assez de participants
if len(participants) < 2:
    print("Il n'y a pas assez de participants pour un tirage au sort.")
else:
    # Faire un tirage au sort de 2 personnes
    gagnants = random.sample(participants, 2)

    # Afficher les gagnants
    print("Les gagnants du tirage au sort sont :")
    for i, gagnant in enumerate(gagnants, start=1):
        print(f"{i}. {gagnant}")