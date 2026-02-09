# 🔄 Control de Flujo en Python

## Funciones

### Lección 8: Definición y Uso de Funciones

Las funciones en Python se definen usando la palabra clave `def` y permiten encapsular código reutilizable.

#### Función Básica
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!
```

#### Función con Valor de Retorno
```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # 7
```

#### Parámetros por Defecto
```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Bob")                   # Hello, Bob!
greet("Bob", greeting="Hi")    # Hi, Bob!
```

#### Número Arbitrario de Argumentos
```python
def sum_all(*args):
    return sum(args)

result = sum_all(1, 2, 3, 4)
print(result)  # 10
```

#### Argumentos con Palabras Clave
```python
def greet(**kwargs):
    name = kwargs.get('name', 'there')
    greeting = kwargs.get('greeting', 'Hello')
    print(f"{greeting}, {name}!")

greet(name="Alice", greeting="Hi")  # Hi, Alice!
```

#### Funciones Lambda
```python
multiply = lambda x, y: x * y
result = multiply(2, 3)
print(result)  # 6
```

#### Ejemplo Práctico
```python
def get_seconds(hours, minutes, seconds):
    return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)  # 11715
```

---

## Condicionales

### Lección 9-10: If, Elif, Else

Los condicionales permiten ejecutar código basado en condiciones.

#### If Simple
```python
def is_positive(number):
    if number > 0:
        return True
```

#### If-Elif-Else
```python
def number_group(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
```

#### Ejemplo: Traductor de Colores
```python
def color_translator(color):
    if color == "red":
        hex_color = "#ff0000"
    elif color == "green":
        hex_color = "#00ff00"
    elif color == "blue":
        hex_color = "#0000ff"
    else:
        hex_color = "unknown"
    return hex_color

print(color_translator("blue"))  # #0000ff
```

#### Ejemplo: Sistema de Calificaciones
```python
def exam_grade(score):
    if score > 95:
        grade = "Top Score"
    elif score >= 60:
        grade = "Pass"
    else:
        grade = "Fail"
    return grade

print(exam_grade(65))   # Pass
print(exam_grade(100))  # Top Score
```

#### Condiciones Múltiples
```python
def format_name(first_name, last_name):
    if first_name != "" and last_name != "":
        return "Name: " + first_name + ", " + last_name  
    elif last_name != "":
        return "Name: " + last_name
    elif first_name != "":
        return "Name: " + first_name
    else:
        return ""
```

---

## Bucles For

### Lección 4-5, 11: Iteración con For

El bucle `for` se usa para iterar sobre secuencias.

#### For Básico
```python
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hello, " + friend)
```

#### Range
```python
for i in range(10):
    print("Hello, World!")
```

#### Iterando sobre Números
```python
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
```

#### Iterando sobre Strings
```python
for char in "Hello":
    print(char)
```

#### Iterando sobre Diccionarios
```python
my_dict = {"a": 1, "b": 2, "c": 3}

# Iterar sobre keys
for key in my_dict:
    print(key)

# Iterar sobre values
for value in my_dict.values():
    print(value)

# Iterar sobre key-value pairs
for key, value in my_dict.items():
    print(key, value)
```

#### Ejemplo: Factorial
```python
def factorial(n):
    result = 1
    for x in range(1, n + 1):
        result = x * result
    return result

print(factorial(5))  # 120
```

#### For-Else
```python
for i in range(3):
    print(i)
else:
    print("Loop completed successfully.")
```

---

## While

### Lección 12: Bucles While

El bucle `while` ejecuta código mientras una condición sea verdadera.

#### While Básico
```python
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")

attempts(10)
```

#### Countdown
```python
def count_down(start_number):
    current = start_number
    while current > 0:
        print(current)
        current -= 1
    print("Zero!")

count_down(3)
```

#### Ejemplo: Factores Primos
```python
def print_prime_factors(number):
    factor = 2
    while factor <= number:
        if number % factor == 0:
            print(factor)
            number = number / factor
        else:
            factor += 1
    return "Done"

print_prime_factors(100)  # 2, 2, 5, 5
```

#### Ejemplo: Potencias de 2
```python
def is_power_of_two(n):
    while n % 2 == 0 and n > 0:
        n = n / 2
    if n == 1:
        return True
    return False

print(is_power_of_two(8))  # True
print(is_power_of_two(9))  # False
```

#### Break Statement
```python
def multiplication_table(number):
    multiplier = 1
    while multiplier <= 5:
        result = multiplier * number 
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1

multiplication_table(8)  # Se detiene en 8x3=24
```

---

## Bucles Anidados

### Lección 13: Nested Loops

Los bucles anidados permiten iteraciones dentro de iteraciones.

#### Ejemplo: Dominó
```python
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()
```

#### Ejemplo: Partidos de Equipos
```python
teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)
```

#### Tabla de Multiplicación
```python
def multiplication_table(start, stop):
    for x in range(start, stop + 1):
        for y in range(start, stop + 1):
            print(str(x * y), end=" ")
        print()

multiplication_table(1, 3)
# 1 2 3 
# 2 4 6 
# 3 6 9
```

---

## Recursión

### Lección 14, 22: Funciones Recursivas

La recursión es cuando una función se llama a sí misma.

#### Factorial Recursivo
```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120
```

#### Fibonacci Recursivo
```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(5):
    print(f"Term {n} = {fibonacci(n)}")
```

#### Tree Traversal
```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

# Ejemplo de árbol
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inorder_traversal(root)  # 4 2 5 1 3
```

⚠️ **Advertencia**: La recursión debe tener siempre un caso base para evitar recursión infinita.

---

## Resumen

En esta sección aprendiste:
- ✅ Definir y usar funciones
- ✅ Parámetros y valores de retorno
- ✅ Condicionales if/elif/else
- ✅ Bucles for y while
- ✅ Bucles anidados
- ✅ Recursión y casos base

💡 **Siguiente paso**: Continúa con [Estructuras de Datos](./03-estructuras-datos.md).
