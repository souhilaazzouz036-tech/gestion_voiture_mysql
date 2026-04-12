from voiture import Voiture

v1 = Voiture("Toyota", "Corolla", 2020, 20000)
v1.afficher_voiture()


from crud_db import connecter_db, supprimer_voiture

conn = connecter_db()
print("Connexion réussie")
conn.close()

from crud_db import ajouter_voiture
from voiture import Voiture

v1 = Voiture("Honda", "Civic", 2021, 22000)
ajouter_voiture(v1)

supprimer_voiture(1)
