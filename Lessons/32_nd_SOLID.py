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

Software Entities must be Open for extention, Closed to be modified


'''

class Notificador:
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError

class NotificadorEmail(Notificador):
    def  Notificar(self):
        print(f"Enviando mensaje por MAIL a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def  Notificar(self):
        print(f"Enviando mensaje por SMS a {self.usuario.email}")

#---------------------------------------------------------------------------------------------------------------------------------------------------
'''

L: LISKOV SUBSTITUTION PRINCIPLE

Si la clase B es una derivada de la clase A. La clase A debería poder ser utilizada en todos los lugarres donde B es utilizada

Subclasses should be substitutable for their base classes without breaking the system.

'''

class Ave:
    def volar(self):
        return "Estoy volando"

class Pinguino(Ave):
    def volar(self):
        return "No puedo volar"

def  hacer_volar(ave = Ave):
    return ave.volar()

print(hacer_volar)

#---------------------------------------------------------------------------------------------------------------------------------------------------

'''

I: INTERFACE SEGREGATION PRINCIPLE

Many smaller, client-specific interfaces are better than one large, general-purpose interface.

No forcemos al cliente a depender de interfaces que no va a utilizar

'''

from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

 class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass
    
class durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass


class Humano(Trabajador, Comedor, durmiente):
    def trabajar(self):
        print("El humano esta trabajando")

    def comer(self):
        print("El humano esta comiendo")

    def dormir(self):
        print("El humano esta durmiendo")

class  Robot(Trabajador):
    def trabajar(self):
        print("El robot esta trabajando")


robocito = robot()

#---------------------------------------------------------------------------------------------------------------------------------------------------

'''

D: DEPENDENCY INVERSION PRINCIPLE
High-level modules shouldn't depend on low-level modules; both should depend on abstractions.

'''

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC)
    @abstractmethod
    def verificar_palabra(self,palabra):
        #Logica para verificar palabras
        pass

class Diccionario(VerificadorOrtografico):
    def verifica_palabra(self,palabra):
        # Logica para verificar las palabras si está en el Diccionario
        pass

class  ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self,palabra):
        #Logica para verificar palabras desde el servicio web
        pass

class CorrectorOrtografico:
    def __init__(self,verificador):
        self.verificador = verificador

    def correfir_texto(self,texto):
        # Usamos el verificador para corregir texto


#- - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


# Bad: Tight coupling
class EmailSender:
    def send(self, message):
        smtp_client = SMTPClient()  # Direct dependency
        smtp_client.send_email(message)

# Good: Dependency on abstraction
class EmailClient:
    def send(self, message):
        raise NotImplementedError()

class SMTPEmailClient(EmailClient):
    def send(self, message):
        # ...    
 
#---------------------------------------------------------------------------------------------------------------------------------------------------
