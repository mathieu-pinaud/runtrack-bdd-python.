import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="Ztssjd_1807", database="LaPlateforme")

cursor = conn.cursor()
cursor.execute("SELECT superficie FROM etage;")
resultat = cursor.fetchall()

superficie = 0

for item in resultat:
    superficie += item[0]

print('La superficie de la Plateforme est de', superficie, 'm2')
cursor.close()
conn.close()