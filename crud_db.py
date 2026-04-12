import mysql.connector
import json

def connecter_db():
    with open("config.json") as f:
        config = json.load(f)

    conn = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )

    return conn

def ajouter_voiture(voiture):
    conn = connecter_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS voiture (
        id INT AUTO_INCREMENT PRIMARY KEY,
        marque VARCHAR(50),
        modele VARCHAR(50),
        annee INT,
        prix DECIMAL(10,2)
    )
    """)

    sql = "INSERT INTO voiture (marque, modele, annee, prix) VALUES (%s, %s, %s, %s)"
    values = (voiture.marque, voiture.modele, voiture.annee, voiture.prix)

    cursor.execute(sql, values)
    conn.commit()

    conn.close()