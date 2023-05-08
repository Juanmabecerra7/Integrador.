from Alumnos import Alumnos
import csv


class ManejadorAlumnos2:
    def __init__(self):
        self.__lista = []

    def agregarAlumno(self, unAlumno):
        self.__lista.append(unAlumno)

    def testAlumnos(self):
        archivo = open("alumnos.csv")
        reader = csv.reader(archivo, delimiter=",")
        for fila in reader:
            dni = fila[0]
            apellido = fila[1]
            nombre = fila[2]
            carrera = fila[3]
            ano_carrera = fila[4]
            unAlumno = Alumnos(dni, apellido, nombre, carrera, ano_carrera)
            self.agregarAlumno(unAlumno)
        archivo.close()

    def getlen(self):
        return len(self.__lista)

    def aprobaron(self, dni):
        indice = 0
        s = ""
        while indice < len(self.__lista):
            if Alumnos.getDni(self.__lista[indice]) == dni:
                s = s + str(Alumnos.getInfo(self.__lista[indice]))
            indice = indice + 1
        return str(s)

    def __str__(self):
        s = ""
        for Alumnos in self.__lista:
            s = s + str(Alumnos) + "\n"
        return 
