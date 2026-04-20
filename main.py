from voiture import Voiture
from crud_db import connecter_db, ajouter_voiture, supprimer_voiture, recuperer_voitures, modifier_voiture


conn = connecter_db()
print("Connexion réussie")
conn.close()
v1 = Voiture("Toyota", "Corolla", 2020, 20000)
v2 = Voiture("Honda", "Civic", 2021, 22000)

ajouter_voiture(v1)
ajouter_voiture(v2)
print("Liste des voitures :")
voitures = recuperer_voitures()
for v in voitures:
    print(v)