from ManejadorAlumno2 import ManejadorAlumnos2
from ManejadorMaterias import ManejadorMaterias

if __name__ == "__main__":
    ma = ManejadorAlumnos2()
    mm = ManejadorMaterias()
    mm.testMaterias()
    print(str(mm))
    ma.testAlumnos()
    print(str(ma))
    opcion = 1
    while opcion != 0:
        print("1: Calcular promedio de un alumno con aplazos y sin aplazos")
        print("2: Calcular los estudiantes que aprobaron una materia")
        print("3: Salir")
        opcion = int(input())
        if opcion == 1:
            dni = str(input("Ingrese el dni del alumno: "))
            print("El promedio es de: ")
            print(mm.calcularPromedio(dni))
        elif opcion == 2:
            materia = str(input("Ingrese el nombre de la materia que: "))
            print("Los Alumnos que Promocionaron la Materia son: ")
            print("DNI APELLIDO Y NOMBRE AÑO NOTA FECHA")
            print(mm.aprobaron(materia, ma))
        elif opcion == 3:
            exit()
        else:
            print("---Opcion Incorrecta---")
        opcion = 1
