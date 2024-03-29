#---------------------------------------------------------------------------------------------------------------------------------------------------

"""
OOO - Abstraction

Abstraction in Python, as in other programming languages, is a concept aimed at handling complexity by hiding unnecessary details from the user. 
It allows programmers to focus on the high-level functionality of a program without needing to understand the intricate details of how each part works.
In Python, abstraction is typically achieved through the use of abstract classes and interfaces.

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------

"""
Abstact Class

Una clase que no podemos instanciar para crear un objeto, pero que nos sirve de plantilla para poder crear otras clases.

Abstract Classes
An abstract class is a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built 
from the abstract class. A class that contains one or more abstract methods is called an abstract class. Abstract methods are those methods that 
generally don’t have an implementation, and they are meant to be overridden in the child classes. Python provides the abc module (Abstract Base 
Classes) to achieve abstraction.


"""

from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años.")

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self):
        print(f"Actualmente estoy en el Rubro de: {self.actividad}")

cristian = Estudiante("Cristian",31,"Masculino","Programador") 
cristian.presentarse()
cristian.hacer_actividad()

pedrito = Trabajador("Pedrito",21,"Masculino","Albañil") 
pedrito.presentarse()
pedrito.hacer_actividad()

#---------------------------------------------------------------------------------------------------------------------------------------------------v

class Persona: 
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    @property
    def nombre(self):
        return self.__nombre

cristian = Persona('Cristian',25)
nombre = cristian.nombre
print(nombre) # Cristian

cristian.nombre = 'Cristian David' # AttributeError: can't set attribute

# El error anterior se debe a que el atributo nombre es privado, por lo que no se puede modificar directamente

#------------------------------------------------------------

# Para solucionar el problema anterior, se puede hacer uso de un decorador setter
class Persona: 
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

#------------------------------------------------------------

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if nombre == '':
            raise ValueError('El nombre no puede estar vacío')
        self.__nombre = nombre
    
    @nombre.deleter
    def nombre(self):
        del self.__nombre

cristian = Persona('Cristian',25)
cristian.nombre = 'Cristian David'
print(cristian.nombre) # Cristian David
del cristian.nombre
print(cristian.nombre) # AttributeError: 'Persona' object has no attribute '_Persona__nombre'
