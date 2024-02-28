#---------------------------------------------------------------------------------------------------------------------------------------------------

"""
OOO - Polymorphism


Polymorphism in programming is the ability of objects of different types to be accessed through the same interface, highlighting a principle in 
OOP (Object-Oriented Programming) that allows methods to do different things based on the object it is acting upon. In Python, polymorphism enables
us to define methods in the child class with the same name as defined in their parent class. As a result, the child class inherits the methods from 
the parent class. However, it is possible to modify a method in a child class that it has inherited from the parent class. This is particularly useful 
in cases where the method inherited from the parent class doesn’t quite fit the child class.

In Python, polymorphism is simple to use because Python being dynamically typed does not require explicit declaration of types. This makes 
polymorphism more natural and easier to implement. Here are some examples demonstrating polymorphism in Python.


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

"""
Dynamic Links


Let's explore dynamic and static linking in the context of Python:

Dynamic Linking

The Standard in Python: Dynamic linking is the default behavior in Python. When you use an import statement to bring in a module, you aren't directly
 embedding the code of that module into your program. Instead, you're creating a reference to it.

Runtime Linking:  At runtime (when your Python program is executed), the Python interpreter searches for the required module and loads it into 
memory. If the module has its own dependencies, those are also loaded.

"""

import datetime

now = datetime.datetime.now()
print(now) 

#---------------------------------------------------------------------------------------------------------------------------------------------------

"""
Static Linking

Less Common in Python: Static linking is less conventional in Python but achievable with specialized tools. It means embedding the code of external libraries directly into your executable file.

Compilation Time: The linking process happens during compilation or packaging.

"""


