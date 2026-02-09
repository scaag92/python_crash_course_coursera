# 📊 Estructuras de Datos en Python

## Tipos de Datos

### Lección 15: Tipos de Datos y Operaciones con Strings

Python ofrece varios tipos de datos fundamentales y operaciones poderosas con strings.

#### Operaciones con Strings

```python
# Indexación
word = "casa"
print(word[0])  # 'c'

# Longitud
text = "Hello, World!"
length = len(text)
print(length)  # 13
```

#### Métodos de String Importantes

```python
# index() - Encuentra la posición de un carácter
word = "supercalifragilisticexpialidocious"
print(word.index('x'))  # 21

# split() - Divide un string en lista
sentence = "Hello World Python"
words = sentence.split()
print(words)  # ['Hello', 'World', 'Python']

# replace() - Reemplaza texto
text = "Hello World"
new_text = text.replace("World", "Python")
print(new_text)  # "Hello Python"
```

#### Formato de Strings

```python
name = "Manny"
number = len(name) * 3
print("Hello {}, Your lucky number is: {}".format(name, number))

# Con nombres
print("Hello {name}, Your lucky number is {number}".format(
    name=name, 
    number=number
))
```

#### Formato con Precisión Decimal

```python
price = 7.5
with_taxes = price * 1.09
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_taxes))
```

---

## Listas

### Lección 16: Operaciones y Métodos de Listas

Las listas son colecciones ordenadas y mutables.

#### Operaciones Básicas

```python
# Crear lista
numbers = [1, 2, 3, 4, 5]

# Acceder elementos
print(numbers[0])  # 1
print(numbers[-1])  # 5 (último elemento)

# Modificar elemento
numbers[0] = 10
print(numbers)  # [10, 2, 3, 4, 5]
```

#### Métodos de Lista

```python
# append() - Agregar al final
list.append(x)

# insert() - Insertar en posición
list.insert(i, x)

# pop() - Remover y retornar elemento
list.pop(i)

# remove() - Remover primera ocurrencia
list.remove(x)

# sort() - Ordenar lista
list.sort()

# reverse() - Invertir orden
list.reverse()

# extend() - Extender con otra lista
list.extend(other_list)
```

#### Ejemplo Práctico

```python
def skip_elements(elements):
    new_list = []
    i = 0
    for element in elements:
        if i < len(elements):
            new_list.append(elements[i])
        i += 2
    return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# ['a', 'c', 'e', 'g']
```

---

## Tuplas

### Lección 17: Tuplas y Enumerate

Las tuplas son colecciones ordenadas e inmutables.

#### Tuplas Básicas

```python
# Crear tupla
coordinates = (10, 20)
file_info = ('Class Assignment', 'docx', 17875)

# Desempaquetado
name, type, size = file_info
print(name)  # 'Class Assignment'
```

#### Enumerate

```python
winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))
# 1 - Ashley
# 2 - Dylan
# 3 - Reese
```

#### Ejemplo: Saltar Elementos

```python
def skip_elements(elements):
    result = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            result.append(element)
    return result

print(skip_elements(["a", "b", "c", "d", "e"]))
# ['a', 'c', 'e']
```

---

## Comprensión

### Lección 18: List Comprehension

La comprensión de listas es una forma concisa de crear listas.

#### Sintaxis Básica

```python
# Forma tradicional
multiples = []
for x in range(1, 11):
    multiples.append(x * 7)

# List comprehension
multiples = [x * 7 for x in range(1, 11)]
print(multiples)  # [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
```

#### Con Condiciones

```python
# Números pares
evens = [x for x in range(0, 101) if x % 2 == 0]

# Números impares
def odd_numbers(n):
    return [x for x in range(1, n + 1) if x % 2 != 0]

print(odd_numbers(10))  # [1, 3, 5, 7, 9]
```

#### Transformaciones

```python
# Longitudes de palabras
languages = ["Python", "Perl", "Ruby", "Go", "Java"]
lengths = [len(language) for language in languages]
print(lengths)  # [6, 4, 4, 2, 4]
```

#### Con If-Else

```python
filenames = ["program.c", "stdio.hpp", "sample.hpp"]
newfilenames = [
    filename[:-2] if ".hpp" in filename else filename 
    for filename in filenames
]
print(newfilenames)  # ["program.c", "stdio.h", "sample.h"]
```

---

## Diccionarios

### Lección 19: Diccionarios y Métodos

Los diccionarios almacenan pares clave-valor.

#### Operaciones Básicas

```python
# Crear diccionario
toc = {"Introduction": 1, "Chapter 1": 4, "Chapter 2": 11}

# Agregar/Modificar
toc["Epilogue"] = 39
toc["Chapter 3"] = 24

# Verificar existencia
print("Chapter 5" in toc)  # False

# Eliminar
del toc["Epilogue"]
```

#### Métodos de Diccionario

```python
file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}

# Iterar sobre keys
for extension in file_counts:
    print(extension)

# Iterar sobre items
for key, value in file_counts.items():
    print(f"{key}: {value}")

# Obtener values
for val in file_counts.values():
    print(val)

# Obtener keys
for k in file_counts.keys():
    print(k)
```

#### Ejemplo: Contador de Letras

```python
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("hello"))
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

#### Métodos Útiles

```python
# update() - Combinar diccionarios
dict1.update(dict2)

# get() - Obtener valor con default
value = dict.get('key', 'default')

# clear() - Limpiar diccionario
dict.clear()

# copy() - Copiar diccionario
new_dict = dict.copy()
```

---

## Generadores

### Lección 20: Generadores con Yield

Los generadores producen valores bajo demanda usando `yield`.

#### Generador Básico

```python
def contador_infinito():
    num = 0
    while True:
        yield num
        num += 1

gen = contador_infinito()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
```

#### Fibonacci Generator

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _, val in zip(range(10), fib):
    print(val, end=" ")
# 0 1 1 2 3 5 8 13 21 34
```

#### Ventajas de Generadores

- 💡 **Eficiencia de Memoria**: No cargan todos los valores en memoria
- 💡 **Lazy Evaluation**: Generan valores solo cuando se necesitan
- 💡 **Secuencias Infinitas**: Pueden representar secuencias infinitas

---

## Ejercicios Prácticos

### Ejercicio 1: Combinar Listas
```python
def combine_lists(list1, list2):
    list1.reverse()
    combined_list = list2 + list1
    return combined_list

Jaimes_list = ["Alma", "Chika", "Benjamin"]
Drews_list = ["Minna", "Carol", "Gunnar"]
print(combine_lists(Jaimes_list, Drews_list))
```

### Ejercicio 2: Grupos por Usuario
```python
def groups_per_user(group_dictionary):
    user_groups = {}
    for group, users in group_dictionary.items():
        for user in users:
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)
    return user_groups
```

---

## Resumen

En esta sección aprendiste:
- ✅ Operaciones con strings y formato
- ✅ Listas y sus métodos
- ✅ Tuplas y enumerate
- ✅ List comprehension
- ✅ Diccionarios y sus operaciones
- ✅ Generadores con yield

💡 **Siguiente paso**: Continúa con [Conceptos Avanzados](./04-avanzado.md).
