# 🎯 Principios SOLID

## Lección 31: Principios de Diseño de Software

SOLID es un acrónimo de cinco principios de diseño orientado a objetos que ayudan a crear software más mantenible, escalable y robusto.

---

## S - Single Responsibility Principle

### Principio de Responsabilidad Única

**Una clase debe tener una única razón para cambiar.**

Cada clase debe tener una sola responsabilidad o funcionalidad. Si una clase tiene múltiples responsabilidades, debe dividirse.

#### ❌ Mal Ejemplo

```python
class Auto:
    def __init__(self):
        self.posicion = 0
        self.combustible = 100
    
    def mover(self, distancia):
        if self.combustible >= distancia / 2:
            self.posicion += distancia
            self.combustible -= distancia / 2
        else:
            print("No hay suficiente combustible")
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
```

**Problema**: La clase Auto maneja tanto el movimiento como el combustible.

#### ✅ Buen Ejemplo

```python
class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

class Auto:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque
    
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("Has movido el auto")
        else:
            print("No hay suficiente combustible")
    
    def obtener_posicion(self):
        return self.posicion

# Uso
tanque = TanqueDeCombustible()
carrito = Auto(tanque)
carrito.mover(10)
print(carrito.obtener_posicion())  # 10
```

💡 **Beneficio**: Cada clase tiene una responsabilidad clara y puede modificarse independientemente.

---

## O - Open/Closed Principle

### Principio Abierto/Cerrado

**Las entidades de software deben estar abiertas para extensión pero cerradas para modificación.**

Debes poder agregar nueva funcionalidad sin modificar el código existente.

#### ❌ Mal Ejemplo

```python
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self, tipo):
        if tipo == "email":
            print(f"Enviando EMAIL a {self.usuario.email}")
        elif tipo == "sms":
            print(f"Enviando SMS a {self.usuario.phone}")
        # Si queremos agregar WhatsApp, debemos modificar esta clase
```

**Problema**: Para agregar un nuevo tipo de notificación, debemos modificar la clase existente.

#### ✅ Buen Ejemplo

```python
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError

class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por EMAIL a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por SMS a {self.usuario.phone}")

class NotificadorWhatsApp(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por WhatsApp a {self.usuario.whatsapp}")
```

💡 **Beneficio**: Puedes agregar nuevos tipos de notificadores sin modificar el código existente.

---

## L - Liskov Substitution Principle

### Principio de Sustitución de Liskov

**Los objetos de una subclase deben poder reemplazar objetos de la superclase sin romper la aplicación.**

Si B es una subclase de A, deberías poder usar B en cualquier lugar donde uses A.

#### ❌ Mal Ejemplo

```python
class Ave:
    def volar(self):
        return "Estoy volando"

class Pinguino(Ave):
    def volar(self):
        return "No puedo volar"  # Rompe el contrato!

def hacer_volar(ave: Ave):
    return ave.volar()

# Problema: Pingüino no puede volar pero hereda de Ave
pinguino = Pinguino()
print(hacer_volar(pinguino))  # "No puedo volar" - comportamiento inesperado
```

#### ✅ Buen Ejemplo

```python
class Ave:
    def moverse(self):
        pass

class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"
    
    def moverse(self):
        return self.volar()

class AveNoVoladora(Ave):
    def caminar(self):
        return "Estoy caminando"
    
    def moverse(self):
        return self.caminar()

class Aguila(AveVoladora):
    pass

class Pinguino(AveNoVoladora):
    pass

def hacer_mover(ave: Ave):
    return ave.moverse()

aguila = Aguila()
pinguino = Pinguino()
print(hacer_mover(aguila))     # "Estoy volando"
print(hacer_mover(pinguino))   # "Estoy caminando"
```

💡 **Beneficio**: Las subclases mantienen el contrato de la superclase.

---

## I - Interface Segregation Principle

### Principio de Segregación de Interfaces

**Muchas interfaces específicas son mejores que una interfaz de propósito general.**

No fuerces a las clases a implementar interfaces que no usan.

#### ❌ Mal Ejemplo

```python
class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass
    
    @abstractmethod
    def comer(self):
        pass
    
    @abstractmethod
    def dormir(self):
        pass

class Robot(Trabajador):
    def trabajar(self):
        print("El robot está trabajando")
    
    def comer(self):
        pass  # Los robots no comen!
    
    def dormir(self):
        pass  # Los robots no duermen!
```

**Problema**: Robot debe implementar métodos que no necesita.

#### ✅ Buen Ejemplo

```python
from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador, Comedor, Durmiente):
    def trabajar(self):
        print("El humano está trabajando")
    
    def comer(self):
        print("El humano está comiendo")
    
    def dormir(self):
        print("El humano está durmiendo")

class Robot(Trabajador):
    def trabajar(self):
        print("El robot está trabajando")

# Uso
robot = Robot()
robot.trabajar()  # El robot está trabajando
```

💡 **Beneficio**: Cada clase implementa solo las interfaces que necesita.

---

## D - Dependency Inversion Principle

### Principio de Inversión de Dependencias

**Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones.**

#### ❌ Mal Ejemplo

```python
class SMTPClient:
    def send_email(self, message):
        print(f"Sending via SMTP: {message}")

class EmailSender:
    def __init__(self):
        self.smtp_client = SMTPClient()  # Dependencia directa!
    
    def send(self, message):
        self.smtp_client.send_email(message)
```

**Problema**: EmailSender depende directamente de SMTPClient. Si queremos cambiar el cliente, debemos modificar EmailSender.

#### ✅ Buen Ejemplo

```python
from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Lógica para verificar en diccionario
        print(f"Verificando '{palabra}' en diccionario")
        return True

class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        # Lógica para verificar online
        print(f"Verificando '{palabra}' online")
        return True

class CorrectorOrtografico:
    def __init__(self, verificador: VerificadorOrtografico):
        self.verificador = verificador
    
    def corregir_texto(self, texto):
        palabras = texto.split()
        for palabra in palabras:
            self.verificador.verificar_palabra(palabra)

# Uso
diccionario = Diccionario()
corrector = CorrectorOrtografico(diccionario)
corrector.corregir_texto("Hola mundo")

# Fácil cambiar a servicio online
servicio = ServicioOnline()
corrector2 = CorrectorOrtografico(servicio)
corrector2.corregir_texto("Hola mundo")
```

#### Otro Ejemplo

```python
from abc import ABC, abstractmethod

class EmailClient(ABC):
    @abstractmethod
    def send(self, message):
        pass

class SMTPEmailClient(EmailClient):
    def send(self, message):
        print(f"Sending via SMTP: {message}")

class SendGridEmailClient(EmailClient):
    def send(self, message):
        print(f"Sending via SendGrid: {message}")

class EmailSender:
    def __init__(self, client: EmailClient):
        self.client = client
    
    def send(self, message):
        self.client.send(message)

# Uso
smtp = SMTPEmailClient()
sender = EmailSender(smtp)
sender.send("Hello")

# Fácil cambiar a SendGrid
sendgrid = SendGridEmailClient()
sender2 = EmailSender(sendgrid)
sender2.send("Hello")
```

💡 **Beneficio**: Fácil cambiar implementaciones sin modificar el código de alto nivel.

---

## Resumen de SOLID

| Principio | Descripción | Beneficio |
|-----------|-------------|-----------|
| **S**ingle Responsibility | Una clase, una responsabilidad | Código más mantenible |
| **O**pen/Closed | Abierto a extensión, cerrado a modificación | Menos bugs al agregar features |
| **L**iskov Substitution | Las subclases deben ser sustituibles | Jerarquías consistentes |
| **I**nterface Segregation | Interfaces específicas, no generales | Clases más simples |
| **D**ependency Inversion | Depender de abstracciones | Código desacoplado y flexible |

---

## Aplicando SOLID

### Ejemplo Completo

```python
from abc import ABC, abstractmethod

# Interface Segregation
class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

# Dependency Inversion
class Notificador(ABC):
    @abstractmethod
    def notificar(self, mensaje):
        pass

# Single Responsibility
class EmpleadoRegular(Trabajador):
    def __init__(self, nombre, notificador: Notificador):
        self.nombre = nombre
        self.notificador = notificador
    
    def trabajar(self):
        print(f"{self.nombre} está trabajando")
        self.notificador.notificar("Trabajo completado")

# Open/Closed - Fácil agregar nuevos notificadores
class NotificadorEmail(Notificador):
    def notificar(self, mensaje):
        print(f"Email: {mensaje}")

class NotificadorSMS(Notificador):
    def notificar(self, mensaje):
        print(f"SMS: {mensaje}")

# Uso
email = NotificadorEmail()
empleado = EmpleadoRegular("Juan", email)
empleado.trabajar()
```

---

## Resumen

En esta sección aprendiste:
- ✅ Single Responsibility Principle
- ✅ Open/Closed Principle
- ✅ Liskov Substitution Principle
- ✅ Interface Segregation Principle
- ✅ Dependency Inversion Principle
- ✅ Cómo aplicar SOLID en código real

💡 **Siguiente paso**: Continúa con [Proyecto Final](./08-proyecto-final.md).
