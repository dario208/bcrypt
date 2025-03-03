import bcrypt  # Correction de 'bycript' en 'bcrypt'

# Création du mot de passe
password = "votre_nouveau_mot_de_passe".encode('utf-8')

# Génération du sel et hachage du mot de passe
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

# Affichage du résultat
print("Mot de passe haché:", hashed.decode('utf-8'))

# Exemple de vérification du mot de passe (optionnel mais recommandé)
if bcrypt.checkpw(password, hashed):
    print("Le mot de passe correspond!")
else:
    print("Le mot de passe ne correspond pas!")