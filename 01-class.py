class MiClase:
    def __mit__(self, parametros01, parametros02):
        self.atributo01 = parametros01
        self.atributo02 = parametros02 

    def metodo (self):
        return "soy un metodo de la clase Miclase"
    

class perro:
    def __init__(self, nombre , raza, edad, color, peso, altura):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.color = color
        self.peso = peso
        self.altura = altura

    def ladrar(self):
        return f'{self.nombre} esta ladrando'
    
    def dormir (self):
        return f'{self.nombre} esta durmiendo'
    
    def info_perro(self):
        return f'hola me llamo {self.nombre},soy un perro de raza {self.raza}, tengo {self.edad}, y soy de colo {self.color}'
    

perro1= perro("Dino","perrosaurio",5,"morado",125,1.75)

print