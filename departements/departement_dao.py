import database
from departements.departement import Departement
class DepartementDao:
    
    connexion = database.connect_db()
    cursor = connexion.cursor()

    def __init__(self) -> None:
        pass
    
    @classmethod
    def create(cls, dpt:Departement):
        sql = "INSERT INTO departement(nom,emplacement,direction) VALUES(%s,%s,%s)"
        params = (dpt.nom,dpt.emplacement,dpt.direction)
        DepartementDao.cursor.execute(sql, params)
        DepartementDao.cursor.close()
        return dpt.nom