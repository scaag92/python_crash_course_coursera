#---------------------------------------------------------------------------------------------------------------------------------------------------

"""
OOO - MRO - Methods Resolution Order

Method Resolution Order (MRO) in Python refers to the sequence in which base classes are searched when executing a method. This order is significant when dealing with multiple inheritance, as it determines how Python will search for a method or attribute if it isn't found in the subclass itself. Python uses the C3 linearization algorithm to determine this order, ensuring that a consistent order is maintained and resolving the potential ambiguities of multiple inheritance.

The MRO ensures that:

A class always appears before its parents.
The order of parent classes is maintained.
If multiple parents inherit from the same grandparent, the grandparent is only visited after all of its children have been.
To view the MRO of a class, you can use the .__mro__ attribute or the mro() method.

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------

# Example 1: Simple Inheritance

class A:
    pass

class B(A):
    pass

print(B.mro())

# This will output:

[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

# It shows that Python looks for methods or attributes in B, then in A, and finally in object, which is the base class for all new-style classes in Python.

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Example 2: Multiple Inheritance
# Consider the following class structure:

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())

# This will output:

[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

# In this example, D inherits from both B and C. The MRO ensures that B is searched before C, and both of these are searched before A, their common parent. This order respects the declaration order of the base classes in D.A
# These examples illustrate how Python's MRO works to resolve method calls in a predictable and consistent manner, which is crucial for understanding and correctly utilizing multiple inheritance.

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Example 3

class A:
    def hablar(self):
        print("Hola desde A")


class B(A):
    def hablar(self):
        print("Hola desde B")

class C(A):
    def hablar(self):
        print("Hola desde C")

class D(B,C):
    def hablar(self):
        print("Hola desde D")

d = D()
d.hablar()

print(D.mro())

# This allow us to define what method to run.
D.hablar(C)

#---------------------------------------------------------------------------------------------------------------------------------------------------

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

