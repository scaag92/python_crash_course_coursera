# 🎓 Proyecto Final - Analizador de Sentimientos

## Lección 32: Proyecto Integrador

Este proyecto final integra múltiples conceptos aprendidos en el curso para crear un analizador de sentimientos usando APIs externas.

---

## Objetivo del Proyecto

Crear un sistema que analice el sentimiento de texto ingresado por el usuario, clasificándolo en categorías desde "Muy Negativo" hasta "Muy Positivo".

---

## Versión 1: Con TextBlob

### Implementación Básica

```python
from textblob import TextBlob

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0: 
            return "Positivo"
        elif analisis.sentiment.polarity == 0: 
            return "Neutro"
        else: 
            return "Negativo"

# Uso
analizer = AnalizadorDeSentimientos()
answer = analizer.analizar_sentimiento("I'm feeling tired")
print(answer)  # Negativo o Neutro
```

### ¿Qué es TextBlob?

TextBlob es una biblioteca de Python para procesamiento de texto que proporciona:
- Análisis de sentimientos
- Clasificación de texto
- Traducción
- Análisis gramatical

### Instalación

```bash
pip install textblob
```

---

## Versión 2: Con OpenAI API

### Implementación Avanzada

```python
import openai

# Configuración
openai.api_key = "tu-api-key-aqui"

system_role = '''
Eres un analizador de sentimientos. Analiza el sentimiento de los mensajes 
y responde con un número entre -1 y 1, donde:
- -1 es negatividad máxima
- 0 es neutral
- 1 es positividad máxima

Puedes usar decimales como 0.3, -0.5, etc.
Solo responde con números (int o float).
'''

mensajes = [{"role": "system", "content": system_role}]

class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    
    def __str__(self):
        return f"\x1b[1;{self.color}m{self.nombre}\x1b[1;37m"

class AnalizadorDeSentimientos:
    def __init__(self, rangos):
        self.rangos = rangos
    
    def analizar_sentimiento(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] <= polaridad <= rango[1]:
                return sentimiento
        return Sentimiento("Muy negativo", "31")

# Definir rangos de sentimientos
rangos = [
    ((-1.0, -0.6), Sentimiento("Muy Negativo", "31")),
    ((-0.6, -0.3), Sentimiento("Negativo", "31")),
    ((-0.3, -0.1), Sentimiento("Algo Negativo", "31")),
    ((-0.1, 0.1), Sentimiento("Neutral", "33")),
    ((0.1, 0.3), Sentimiento("Algo Positivo", "32")),
    ((0.3, 0.9), Sentimiento("Positivo", "32")),
    ((0.9, 1.0), Sentimiento("Muy Positivo", "32"))
]

analizador = AnalizadorDeSentimientos(rangos)

# Loop principal
while True:
    user_prompt = input("Dime algo: ")
    
    if user_prompt.lower() == 'salir':
        break
    
    mensajes.append({"role": "user", "content": user_prompt})
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=mensajes,
        max_tokens=8
    )
    
    respuesta = completion.choices[0].message['content']
    mensajes.append({"role": "assistant", "content": respuesta})
    
    try:
        sentimiento = analizador.analizar_sentimiento(float(respuesta))
        print(sentimiento)
    except ValueError:
        print("Error al procesar la respuesta")
```

---

## Conceptos Aplicados

### 1. Programación Orientada a Objetos

```python
class Sentimiento:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    
    def __str__(self):  # Método especial
        return f"\x1b[1;{self.color}m{self.nombre}\x1b[1;37m"
```

**Conceptos usados:**
- Clases y objetos
- Constructor `__init__`
- Método especial `__str__`
- Encapsulación de datos

---

### 2. Principios SOLID

#### Single Responsibility
```python
# Clase Sentimiento: Solo representa un sentimiento
class Sentimiento:
    pass

# Clase AnalizadorDeSentimientos: Solo analiza sentimientos
class AnalizadorDeSentimientos:
    pass
```

#### Dependency Inversion
```python
# El analizador depende de abstracciones (rangos), no de implementaciones concretas
class AnalizadorDeSentimientos:
    def __init__(self, rangos):
        self.rangos = rangos  # Inyección de dependencias
```

---

### 3. Estructuras de Datos

```python
# Lista de tuplas con rangos y sentimientos
rangos = [
    ((-1.0, -0.6), Sentimiento("Muy Negativo", "31")),
    ((-0.6, -0.3), Sentimiento("Negativo", "31")),
    # ...
]

# Diccionario para mensajes de chat
mensajes = [
    {"role": "system", "content": system_role},
    {"role": "user", "content": user_prompt}
]
```

---

### 4. Control de Flujo

```python
# While loop para interacción continua
while True:
    user_prompt = input("Dime algo: ")
    
    if user_prompt.lower() == 'salir':
        break
    
    # Procesamiento...
```

---

### 5. Manejo de Excepciones

```python
try:
    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    print(sentimiento)
except ValueError:
    print("Error al procesar la respuesta")
```

---

## Mejoras Sugeridas

### 1. Agregar Logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self, polaridad):
        logger.info(f"Analizando polaridad: {polaridad}")
        # ...
```

### 2. Persistencia de Datos

```python
import json

class HistorialSentimientos:
    def __init__(self, archivo='historial.json'):
        self.archivo = archivo
        self.historial = []
    
    def agregar(self, texto, sentimiento):
        self.historial.append({
            'texto': texto,
            'sentimiento': sentimiento,
            'timestamp': datetime.now().isoformat()
        })
    
    def guardar(self):
        with open(self.archivo, 'w') as f:
            json.dump(self.historial, f, indent=2)
```

### 3. Interfaz Gráfica

```python
import tkinter as tk

class InterfazAnalizador:
    def __init__(self, analizador):
        self.analizador = analizador
        self.root = tk.Tk()
        self.root.title("Analizador de Sentimientos")
        
        # Widgets
        self.texto_input = tk.Entry(self.root, width=50)
        self.boton_analizar = tk.Button(
            self.root, 
            text="Analizar", 
            command=self.analizar
        )
        self.resultado_label = tk.Label(self.root, text="")
        
        # Layout
        self.texto_input.pack()
        self.boton_analizar.pack()
        self.resultado_label.pack()
    
    def analizar(self):
        texto = self.texto_input.get()
        resultado = self.analizador.analizar_sentimiento(texto)
        self.resultado_label.config(text=str(resultado))
    
    def run(self):
        self.root.mainloop()
```

### 4. Tests Unitarios

```python
import unittest

class TestAnalizadorDeSentimientos(unittest.TestCase):
    def setUp(self):
        rangos = [
            ((-1.0, -0.1), Sentimiento("Negativo", "31")),
            ((-0.1, 0.1), Sentimiento("Neutral", "33")),
            ((0.1, 1.0), Sentimiento("Positivo", "32"))
        ]
        self.analizador = AnalizadorDeSentimientos(rangos)
    
    def test_sentimiento_positivo(self):
        resultado = self.analizador.analizar_sentimiento(0.5)
        self.assertEqual(resultado.nombre, "Positivo")
    
    def test_sentimiento_negativo(self):
        resultado = self.analizador.analizar_sentimiento(-0.5)
        self.assertEqual(resultado.nombre, "Negativo")
    
    def test_sentimiento_neutral(self):
        resultado = self.analizador.analizar_sentimiento(0.0)
        self.assertEqual(resultado.nombre, "Neutral")

if __name__ == '__main__':
    unittest.main()
```

---

## Dependencias del Proyecto

### requirements.txt

```txt
textblob==0.17.1
openai==0.27.0
python-dotenv==1.0.0
```

### Instalación

```bash
pip install -r requirements.txt
```

---

## Variables de Entorno

### .env

```env
OPENAI_API_KEY=tu-api-key-aqui
```

### Uso en código

```python
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
```

---

## Estructura del Proyecto

```
proyecto-final/
├── src/
│   ├── __init__.py
│   ├── analizador.py
│   ├── sentimiento.py
│   └── interfaz.py
├── tests/
│   ├── __init__.py
│   └── test_analizador.py
├── .env
├── requirements.txt
├── README.md
└── main.py
```

---

## Ejecución

```bash
# Versión básica
python main.py

# Con tests
python -m pytest tests/

# Con coverage
python -m pytest --cov=src tests/
```

---

## Resumen

Este proyecto final demuestra:
- ✅ Integración de APIs externas
- ✅ Programación Orientada a Objetos
- ✅ Principios SOLID
- ✅ Manejo de entrada/salida
- ✅ Estructuras de datos complejas
- ✅ Control de flujo avanzado
- ✅ Manejo de excepciones
- ✅ Buenas prácticas de desarrollo

💡 **Siguiente paso**: Explora los [Desafíos Prácticos](./09-challenges.md) para aplicar tus conocimientos en escenarios cloud/DevOps.
