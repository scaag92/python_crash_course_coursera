#---------------------------------------------------------------------------------------------------------------------------------------------------

"""
OOO - Encapsulation 

Encapsulation is a fundamental concept in object-oriented programming (OOP) that involves bundling of data (attributes) and methods (functions) that 
operate on the data into a single unit, or class. In Python, encapsulation is used to restrict access to methods and variables. This prevents data 
from direct modification which is called information hiding.

In Python, encapsulation is implemented using private and protected members (variables and methods). Here's how it works:

Private members: Private members are defined by prefixing the name with two underscores __. They can't be accessed directly from outside the class 
but can be accessed within the class.

Protected members: Protected members are defined by prefixing the name with a single underscore _. They are intended to be used only within the 
class and its subclasses. It's more of a convention than enforced by the language.


"""
#---------------------------------------------------------------------------------------------------------------------------------------------------

# Example 1: Using Private Members

class Car:
    def __init__(self):
        self.__make = "Toyota"  # Private Variable
        self.__model = "Corolla"  # Private Variable

    def get_car_details(self):
        return f"Make: {self.__make}, Model: {self.__model}"

    def set_car_details(self, make, model):
        self.__make = make
        self.__model = model

# Creating an object
my_car = Car()

# Accessing the method that uses private variables
print(my_car.get_car_details())  # Make: Toyota, Model: Corolla

# Trying to access private variable directly (This will raise an error)
# print(my_car.__make)  # AttributeError: 'Car' object has no attribute '__make'

# Updating car details
my_car.set_car_details("Honda", "Civic")
print(my_car.get_car_details())  # Make: Honda, Model: Civic


#---------------------------------------------------------------------------------------------------------------------------------------------------

# Example 2: Using Protected Members

class Computer:
    def __init__(self):
        self._brand = "Lenovo"  # Protected Variable

class Laptop(Computer):
    def __init__(self):
        super().__init__()
        self._type = "ThinkPad"  # Protected Variable

    def get_details(self):
        return f"Brand: {self._brand}, Type: {self._type}"

# Creating an object of subclass
my_laptop = Laptop()

# Accessing protected members through a method
print(my_laptop.get_details())  # Brand: Lenovo, Type: ThinkPad

# Accessing protected variable directly (Not recommended, but possible)
print(my_laptop._brand)  # Lenovo

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Getters

class  Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre


cristian = Persona()
nombre = cristian.get_nombre()
print(nombre) 

#---------------------------------------------------------------------------------------------------------------------------------------------------       

# Setters

class  Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

    def set_nombre(self, new_nombre):
        self.set__nombre = new_nombre


cristian = Persona()
cristian.get_nombre() = juanito
print(nombre) 

#---------------------------------------------------------------------------------------------------------------------------------------------------
"""
DECORADOR PROPERTY
Python decorador property is a built-in decorator that creates a property object from a method. And it allows us to define a method that can be accessed like an attribute, instead of like a method.

The Property Decorator: Attributes in Disguise

The @property decorator in Python provides a sleek way to make class attributes behave like methods. In essence, it lets you define methods that are accessed as if they were simple attributes, without using the parentheses typical of method calls.

Why Use the Property Decorator?
1 - Abstraction and Control:  The @property decorator lets you control how an attribute is accessed and modified.

2 - Calculated Attributes  You can define attributes that are calculated on the fly rather than storing a direct value.

3 -  Cleaner Code:  Using properties makes your code more readable and aligns with the principle of object-oriented programming by encapsulating behavior within your classes.
"""

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

#---------------------------------------------------------------------------------------------------------------------------------------------------

