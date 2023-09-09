class Alumno:
    def __init__(self,nombre): #constructor#
        self.nombre= nombre
        self.calificaciones = []

    def agregar_calificaciones(self,calificacion): #metodos#
        self.calificaciones.append(calificacion)

    def calculr_promedio(self): #metodos#
        if len(self.calificaciones)==0:
            return 0
        else:
            return sum(self.calificaciones)/len(self.calificaciones)

#TODOS LOS ARREGLOS NO SE DECLARAN EN EL CONSTRUCTOR

class RegistrosAlumnos:
    def __init__(self):
        self.alumnos = []

    #Def metodos
    def agregar_alumno(self,nombre):
        alumno= Alumno(nombre)
        self.alumnos.append(alumno)

    def buscar_alumno(self,nombre):
        for alumno in self.alumnos:
            if alumno.nombre == nombre:
                return alumno
        return None

    def mostrar_informacion(self):
        for alumno in self.alumnos:
            print(f'Nombre {alumno.nombre}')
            print("Calficaciones:",alumno.calificaciones)
            print(f'Promedio de notas {alumno.calcular_promedio()}')
            print("\n")


registros = RegistrosAlumnos()

while True:
    print("1. Agregar Alumno")
    print("2. Agregar calificacion Alumno")
    print("3. Mostrar informacion de todos los Alumnos")
    print("4. Salir")

    opcion= int(input("Seleccione una opcion"))

    if opcion == 1:
        nombre = input("Agregue el nombre del Alumno:")
        registros.agregar_alumno(nombre)

    elif opcion == 2:
        nombre = input("Ingrese el nombre del Alumno:")
        alumno = registros.buscar_alumno(nombre)
        if alumno:
            calificacion =float(input("Ingrese la calificacion"))
            alumno.agregar_calificaciones(calificacion)
        else:
            print("Alumno no encontrado")

    elif opcion == 3:
     registros.mostrar_informacion()

    elif opcion == 4:
        break

    else:
        print("opcion no es valida")

