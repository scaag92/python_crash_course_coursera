# GENERATORS

""" 
Generator is a function that allows a sequence of values to be generated over time. Instead of returning all values at once (as a list would), 
a generator produces a value and then suspends its state so that it can be resumed later. This is accomplished by using the yield keyword instead of return.

Generators are very useful when working with large data streams that you do not want to load completely into memory, or when the computational 
cost of generating each value is high and you want to do it only on demand.

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------

def contador_infinito():
    num = 0
    while True:
        yield num
        num += 1

gen = contador_infinito()

print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
# Esto puede continuar tanto como desees.

#---------------------------------------------------------------------------------------------------------------------------------------------------

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()

for _, val in zip(range(10), fib):
    print(val, end=" ")
# Salida: 0 1 1 2 3 5 8 13 21 34

#---------------------------------------------------------------------------------------------------------------------------------------------------

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()

for _, val in zip(range(10), fib):
    print(val, end=" ")
# Salida: 0 1 1 2 3 5 8 13 21 34

#---------------------------------------------------------------------------------------------------------------------------------------------------



