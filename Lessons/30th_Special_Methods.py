#---------------------------------------------------------------------------------------------------------------------------------------------------

"""
Special Methods

Are instance methods that are reserved by Python and affect an object’s high-level behavior and interactions with operators. These methods allow us 
to customize how our classes behave in various contexts. 

Nos permite crear el objeto cuando invocamos la funció
Devolvernos una representación del objeto en una cadena de texto

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------

'''

Constructor and Initialization

__init__(self, ...):  The constructor. Called when an instance of your class is created. Used to initialize the object's attributes.

'''

class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(42)


#---------------------------------------------------------------------------------------------------------------------------------------------------

'''
Representation

__str__(self):  Controls the informal string representation of an object. Called when you use str(object) or print(object).

'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age} years old)"

#---------------------------------------------------------------------------------------------------------------------------------------------------

'''

__repr__(self):  Controls the official string representation of an object. Often used for debugging. Should ideally be unambiguous.

'''

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"


#---------------------------------------------------------------------------------------------------------------------------------------------------

'''

Operators and Comparisons

__add__(self, other):  Implements the + operator.

__sub__(self, other):  Implements the - operator.

__eq__(self, other): Implements the == operator.

__lt__(self, other): Implements the < operator.

And many others! (__mul__, __gt__, __len__, etc.)

'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


#---------------------------------------------------------------------------------------------------------------------------------------------------

'''

Context Managers

__enter__(self):  Sets up the context for a with statement.

__exit__(self, exc_type, exc_val, exc_tb):  Cleans up after the with statement, even if exceptions occur.

'''

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


#---------------------------------------------------------------------------------------------------------------------------------------------------

class Personaje():
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__ (self):
        return f"Nommbre: {self.nombre}     Fuerza:{self.fuerza}    Velocidad:{self.velocidad}"

    def __add__(self,nuevo_objeto):
        nuevo_nombre = self.nombre + "-" + nuevo_objeto.nombre
        nuevo_fuerza = round(((self.fuerza + nuevo_objeto.fuerza)/2)**2)
        nuevo_velocidad = round(((self.velocidad + nuevo_objeto.velocidad)/2)**2)
        return Personaje(nuevo_nombre, nuevo_fuerza, nuevo_velocidad)

goku = Personaje("Goku",100,100)
vegeta = Personaje("Vegeta",80,80)
gogueta = goku + vegeta

print(gogueta)

#---------------------------------------------------------------------------------------------------------------------------------------------------
