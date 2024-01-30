#Simple Inheritance
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("Hola Estoy hablando")

class Empleado(Persona):
    #Se usa pass cuando queremos crear algo pero no aún que va ha hacer
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
   
roberto = Empleado("Roberto",43,"Argentino","Developer","UnMillon")

roberto.hablar()
print(roberto.nombre())
