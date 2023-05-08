from Materias import Materias
import csv


class ManejadorMaterias:
    def __init__(self):
        self.__listaM = []

    def agregarMateria(self, unaMateria):
        self.__listaM.append(unaMateria)

    def testMaterias(self):
        archivo = open("materiasAprobadas.csv")
        reader = csv.reader(archivo, delimiter=",")
        for fila in reader:
            dni = fila[0]
            nombre_materia = fila[1]
            fecha = fila[2]
            nota = fila[3]
            aprobacion = fila[4]
            unaMateria = Materias(dni, nombre_materia, fecha, nota, aprobacion)
            self.agregarMateria(unaMateria)
        archivo.close()

    def calcularPromedio(self, dni):
        promedio = 0
        indice = 0
        while indice < len(self.__listaM):
            if Materias.getDni(self.__listaM[indice]) == str(dni):
                promedio = int(Materias.getNota(self.__listaM[indice]))
            indice = indice + 1
        return promedio

    def aprobaron(self, materia, ma):
        indice = 0
        s = ""
        alum = ""
        while indice < len(self.__listaM):
            if str(Materias.getNombre(self.__listaM[indice])) == str(materia) and str(Materias.getAprobacion(self.__listaM[indice])) >= "P":
                dni = Materias.getDni(self.__listaM[indice])
                alum = str(ma.aprobaron(dni))
                s = s + str(alum +" "+Materias.getNota(self.__listaM[indice])+" "+Materias.getFecha(self.__listaM[indice])) + "\n"
            indice = indice + 1
        return str(s)

    def __str__(self):
        s = ""
        for Materias in self.__listaM:
            s = s + str(Materias) + "\n"
        return str(s)
