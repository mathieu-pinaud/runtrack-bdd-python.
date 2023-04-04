import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="Ztssjd_1807", database="LaPlateforme")

cursor = conn.cursor()
cursor.execute("SELECT capacite FROM salle;")
resultat = cursor.fetchall()

capacite = 0

for item in resultat:
    capacite += item[0]

print('La capacite de toutes est de :', capacite)
cursor.close()
conn.close()