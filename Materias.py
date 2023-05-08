class Materias:
    __dni = ""
    __nombre_materia = ""
    __fecha = ""
    __nota = ""
    __aprobacion = ""

    def __init__(self, dni, nombre_materia, fecha, nota, aprobacion):
        self.__dni = dni
        self.__nombre_materia = nombre_materia
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = aprobacion

    def getFecha(self):
        return str(self.__fecha)

    def getNota(self):
        return str(self.__nota)

    def getDni(self):
        return str(self.__dni)

    def getAprobacion(self):
        return str(self.__aprobacion)

    def getNombre(self):
        return str(self.__nombre_materia)

    def __str__(self):
        return str(self.__dni+" "+self.__nombre_materia+" "+self.__fecha+" "+self.__nota+" "+self.__aprobacion+" ")
