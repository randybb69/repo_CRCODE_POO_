class Calculadora:
    def __init__(self,parametro1,parametro2):
        self.num1 = parametro1
        self.num2 = parametro2

    def suma(self):
        return self.num1 + self.num2
    def resta (self):
        return self.num1 - self.num2
    def multiplicacion (self):
        return self.num1 * self.num2
    def division (self):
        if self.num2 !=0:
            return self.num1 / self.num2
        else:
            return"No se puede retornar"
        
numeros= Calculadora(25,5)

print("suma: ", numeros.suma())
print("resta: ", numeros.resta())
print("multiplicacion: ", numeros.multiplicacion())
print("division: ", numeros.division())
        
    
