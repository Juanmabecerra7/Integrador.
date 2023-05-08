class Alumnos:
    __dni = ""
    __apellido = ""
    __nombre = ""
    __carrera = ""
    __ano_carrera = ""

    def __init__(self, dni, apellido, nombre, carrera, ano_carrera):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__ano_carrera = ano_carrera

    def getDni(self):
        return str(self.__dni)

    def getInfo(self):
        return str(self.__dni+" "+self.__apellido+" "+self.__nombre+" "+self.__ano_carrera)

    def __str__(self):
        return str(self.__dni+" "+self.__apellido+" "+self.__nombre+" "+self.__carrera+" "+self.__ano_carrera+" ")
