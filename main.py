from voiture import Voiture

v1 = Voiture("Toyota", "Corolla", 2020, 20000)
v1.afficher_voiture()


from crud_db import connecter_db

conn = connecter_db()
print("Connexion réussie")
conn.close()
