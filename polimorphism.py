""""
Polimorphism

Polymorphism derives from Greek, meaning "many forms." In programming, it means using the same interface (functions, methods, operators) for objects of different types and having the correct behavior  invoked depending 
on the type of object. This leads to more flexible and adaptable code.

Types of Polymorphism in Python

Duck Typing:  Python focuses on an object's capabilities rather than its strict type.  If an object has a certain method, Python assumes it can be used, regardless of class hierarchy.

Operator Overloading: Operators like +, -, etc., can have different behaviors depending on the data types involved.

Method Overloading: Python doesn't support traditional method overloading (multiple methods with the same name but different parameter lists within the same class). However,  you can simulate it with default arguments 
and variable argument lists.

Method Overriding (Inheritance): Subclasses can redefine methods inherited from their parent class, customizing behavior.

Examples

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------
""""
Enlaces dinamicos
Enlaces estaticos

Tipo real
Tipo declarado
"""
#---------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Duck Typing

class Duck:
    def quack(self):
        print("Quack!")

class Dog:
    def quack(self):
        print("Woof!")

def make_it_quack(obj):
    obj.quack()

make_it_quack(Duck())  # Output: Quack!
make_it_quack(Dog())  # Output: Woof!

#---------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Operator Overloading

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(2, 3)
v2 = Vector(5, -1)
v3 = v1 + v2  
print(v3.x, v3.y)  # Output: 7 2

#---------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Method Overriding (Inheritance)

class Animal:
    def speak(self):
        print("Generic animal sound")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Dog(Animal):
    def speak(self):
        print("Woof!")

pet1 = Cat()
pet2 = Dog()

pet1.speak()  # Output: Meow!
pet2.speak()  # Output: Woof!

#---------------------------------------------------------------------------------------------------------------------------------------------------
