import mysql.connector

class GrudSalarié():
    def __init__(self):
        pass
    def generate(self, cursor, connecteur, nom, prenom, salaire, service_id):
        cursor.execute("INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s);", (nom, prenom, salaire, service_id))
        connecteur.commit()
    def read(self, cursor):
        cursor.execute("SELECT * FROM employes;")
        resultat = cursor.fetchall()
        print(resultat)
    def update(self, cursor, connecteur, colonne, valeur, id):
        cursor.execute("UPDATE employes SET %s = %s WHERE id = %s;", (colonne, valeur, id))
        connecteur.commit()
    def delete_id(self, cursor, connecteur, id):
        cursor.execute("DELETE FROM employes WHERE id = %s", (id,))
        connecteur.commit()

connecteur = mysql.connector.connect(host="localhost", user="root", password="Ztssjd_1807", database="LaPlateforme")

cursor = connecteur.cursor()
cursor.execute("SELECT * FROM employes WHERE salaire > 3000;")
resultat = cursor.fetchall()
print(resultat,'\n')

cursor.execute("SELECT * FROM employes;")
liste_employe = cursor.fetchall()
for item in liste_employe:
    cursor.execute("SELECT nom FROM services WHERE id = %s", (item[4],))
    service = cursor.fetchone()
    print(item[0], item[1], service)

mon_grud = GrudSalarié()
mon_grud.read(cursor)
mon_grud.generate(cursor, connecteur, 'Louis', 'Louis', 0, 2)
mon_grud.read(cursor)
mon_grud.update(cursor, connecteur, 'nom', 'Louise', 6)
mon_grud.read(cursor)
mon_grud.delete_id(cursor, connecteur, 6)
mon_grud.read(cursor)
cursor.close()
connecteur.close()