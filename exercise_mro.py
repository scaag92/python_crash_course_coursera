#---------------------------------------------------------------------------------------------------------------------------------------------------

from typing import ClassVar


class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def datos(self):
        print(f'El nombre es: {self.nombre} y la edad {self.edad}')

class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        Persona.__init__(self,nombre,edad)
        self.grado = grado
    
    def imprimir(self):
        print(f'El grado del estudiante {self.nombre} es: {self.grado}')


Estudiante1 = Estudiante('Juan','24','Decimo') 
Estudiante1.imprimir()
Estudiante1.datos()

#---------------------------------------------------------------------------------------------------------------------------------------------------

class Animal():
    def comer(self):
        print('El animal esta comiendo')

class Ave(Animal):
    def volar(self):
        print('El animal esta volando')

class Mamifero(Animal):
    def amamantar(self):
        print('El animal esta amamantando')

class Murcielago(Mamifero,Ave):
    pass

ave = Murcielago()
ave.comer()
ave.amamantar()
ave.volar()

#---------------------------------------------------------------------------------------------------------------------------------------------------
