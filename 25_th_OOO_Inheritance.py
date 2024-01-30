#---------------------------------------------------------------------------------------------------------------------------------------------------

"""
OOO - Inheritance

Inheritance in Python is a fundamental concept in object-oriented programming (OOP) that allows a new class, known as a child class, to inherit 
attributes and methods from an existing class, known as a parent class. This makes it easier to create and maintain applications by enabling code 
reusability and a hierarchical organization of classes.

Here's a basic overview of how inheritance works in Python:

1 - Defining a Parent Class: A parent class, also known as a base or superclass, is a class that is being inherited from. It includes methods and 
attributes that will be available to the child class.

class Parent:
    def __init__(self):
        self.value = "Inside Parent"

    def show(self):
        print(self.value)

2 - Creating a Child Class: A child class, also known as a subclass, is a class that inherits from the parent class. It can add new methods and 
attributes or override existing ones.

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value = "Inside Child"

    def display(self):
        print(self.value)

super().__init__() is used to call the constructor of the parent class.
The Child class overrides the value attribute from the Parent class.

3 - Using Inheritance: When you create an instance of the child class, it will inherit the methods and attributes from the parent class.

obj = Child()
obj.show()    # Accessing method from the parent class
obj.display() # Accessing method from the child class

4 - Types of Inheritance:
    -   Single Inheritance: Where a child class inherits from one parent class.
    -   Multiple Inheritance: Where a child class inherits from multiple parent classes.
    -   Multilevel Inheritance: A form of inheritance where a class is derived from a class which is also derived from another class.
    -   Hierarchical Inheritance: Several child classes inherit from a single parent class.

5 - Method Overriding: This is when the child class provides a specific implementation for a method that is already defined in its parent class. 
This allows you to customize or extend the behavior of the parent class method.

6 - Method Overloading: Python does not support method overloading like other languages (e.g., Java or C++). However, you can achieve similar 
functionality using default arguments or variable-length arguments.

"""

#---------------------------------------------------------------------------------------------------------------------------------------------------

"""


"""
#---------------------------------------------------------------------------------------------------------------------------------------------------


class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))

class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()

#---------------------------------------------------------------------------------------------------------------------------------------------------

class Celular:
    def __init__(self,marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self):
        print(f'Estas haciendo una llamada desde un: {self.modelo}')

    def colgar(self):
        print(f'Cortaste la llamada desde un: {self.modelo}')


celular1 = Celular("Samsung","S50","50MP")
celular2 = Celular("Iphone","15Pro","100MP",)

print(celular1.marca)

#---------------------------------------------------------------------------------------------------------------------------------------------------

celular1.llamar()
class estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f'El estudiante {self.nombre} esta estudiando' )

x = input('Enter your name: ')
age = input('Enter your age: ')
gr = input('Enter your grade: ')

estudiante1 = estudiante(x,age,gr)
estudiante1.estudiar()

#---------------------------------------------------------------------------------------------------------------------------------------------------



