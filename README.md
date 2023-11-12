# Python Essentials Repository

This repository is a comprehensive guide to some of the fundamental concepts of Python programming. It includes examples and explanations of various Python constructs and data types.

## Contents

- `If` Statements
- `For` Loops
- `While` Loops
- Nested `For` Loops
- Recursion
- Data Types
- Lists
- Tuples
- List Comprehension
- Dictionaries
- Generators
- Decorators
- Input Handling
- Explicit Conversion
- Functions

Each topic is contained in its own Python script with detailed comments explaining the functionality.

### If Statements

```python
# Example of if-elif-else
x = 10
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is exactly 10")
else:
    print("x is less than 10")
```

### Else
# Example of for loop
```python

for i in range(5):
    print(i)

```

### While Loop
# Example of while loop
```python

count = 0
while count < 5:
    print(count)
    count += 1

```

### Nested Loop
# Example of nested for loop
```python

for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

```

# Example of nested for loop
```python

for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

```

# Example of recursion
```python

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

```
