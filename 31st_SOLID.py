#---------------------------------------------------------------------------------------------------------------------------------------------------
'''
SOLID Principles

Are a series of good practices that will make you write better quality software

SOLID stands for:

S: Single responsibility principle
O: Open/Closed principle
L: Liskov’s substitution principle
I: Interface segregation principle
D: Dependency inversion principle

#---------------------------------------------------------------------------------------------------------------------------------------------------

S: SINGLE RESPONSABILITY PRINCIPLE

Una clase debería tener una responsabilidad unica y si llega a tener varias, se debe dividir. Evita que los desarrolladores creen clases sobre cargadas
o multi funcionadas. Si limitamos las clases a una unica funcionabilidad, el código se vuelve mas limpio y facil de mantener. Es importante que esta
clase pueda realizar su tarea sin depender de otra clase.

'''

class Auto():
    def __init__(self,tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self,distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible( distancia /2 )
            print("Has movido el auto")
        else:
            print("No hay suficiente combustible")

    def obtener_posicion(self):
        return self.posicion

 
class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self,cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self,cantidad):
        self.combustible -= cantidad

       

tanque = TanqueDeCombustible()
carrito = Auto(tanque)

print(carrito.obtener_posicion())
print(carrito.mover(10))
print(carrito.obtener_posicion())
print(carrito.mover(20))
print(carrito.obtener_posicion())
print(carrito.mover(60))
print(carrito.obtener_posicion())
print(carrito.mover(100))
print(carrito.obtener_posicion())
print(carrito.mover(90))

#---------------------------------------------------------------------------------------------------------------------------------------------------

'''

O: OPEN / CLOSED PRINCIPLE

'''






#---------------------------------------------------------------------------------------------------------------------------------------------------
