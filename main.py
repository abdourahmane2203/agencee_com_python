from employes.employe_dao import EmployeDao
from departements.departement_dao import DepartementDao
from employes.employe import Employe
from departements.departement import Departement

emp1 = Employe("Diallo","Abdou","AD0027","Dev Web","IT")
(employes, message) = EmployeDao.list_all()
print(message, employes)

data_emp = EmployeDao.create(emp1)
print(data_emp)

#dpt = Departement('IT','2eme etage', 'Labrie')
#data = DepartementDao.create(dpt)

#print(data)

