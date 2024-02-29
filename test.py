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

#This code will create a calculator that can add, subtract, multiply, and divide. From the user input, the program will determine which operation to complete. The program will then return the result of the operation. If the user does not input a valid operation, the program will notify the user.

class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, num1, num2):
        self.result = num1 + num2
    def subtract(self, num1, num2):
        self.result = num1 - num2
    def divide(self, num1, num2):
        self.result = num1 / num2
    def multiply(self, num1, num2):
        self.result = num1 * num2

calculator = Calculator()
operation = input('What operation would you like to complete? ')
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
if operation == 'add':
    calculator.add(num1, num2)
    print(calculator.result)
elif operation == 'subtract':
    calculator.subtract(num1, num2)
    print(calculator.result)
elif operation == 'divide':
    calculator.divide(num1, num2)
    print(calculator.result)
elif operation == 'multiply':
    calculator.multiply(num1, num2)
    print(calculator.result)
else:
    print('Invalid operation')

#------------------------------------------------------------


