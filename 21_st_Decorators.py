#---------------------------------------------------------------------------------------------------------------------------------------------------

# DECORATORS

"""

Decorators in Python serve as a versatile and powerful tool for extending or modifying the behavior of functions and classes without
altering their actual code. They are essentially higher-order functions that take another function or class as input and return a 
modified or enhanced version of it. This feature allows for more readable, maintainable, and reusable code

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------
# 1 - Logging and Debugging: Decorators can be used to add logging capabilities to a function, which can help in debugging or tracking function usage.

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(3, 4)

#---------------------------------------------------------------------------------------------------------------------------------------------------
# 2 - Performance Measurement: Decorators can be utilized to measure the execution time of a function, which is helpful for performance testing.

import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function(delay_time):
    time.sleep(delay_time)

slow_function(2)

#---------------------------------------------------------------------------------------------------------------------------------------------------
# 3 - Authorization and Authentication: Decorators can enforce checks before executing a function, such as verifying permissions or user roles.

def admin_only(func):
    def wrapper(*args, **kwargs):
        if not user_is_admin():
            raise Exception("This function can only be used by admin users.")
        return func(*args, **kwargs)
    return wrapper

@admin_only
def sensitive_function():
    print("Sensitive data accessed.")

# Assume user_is_admin() checks whether the current user is an admin

#---------------------------------------------------------------------------------------------------------------------------------------------------
# 4 - Caching or Memoization: Implementing caching strategies to save results of expensive function calls and return the cached result when the same inputs occur again.

def admin_only(func):
    def wrapper(*args, **kwargs):
        if not user_is_admin():
            raise Exception("This function can only be used by admin users.")
        return func(*args, **kwargs)
    return wrapper

@admin_only
def sensitive_function():
    print("Sensitive data accessed.")

# Assume user_is_admin() checks whether the current user is an admin

#---------------------------------------------------------------------------------------------------------------------------------------------------

def  decorator(function):
    def funcion_modificada():
        print("Antes de ejecutar la funcion")
        function()
    return funcion_modificada

def saludo():
    print("Hola")

saludo_modificado = decorator(saludo)
saludo_modificado()

#---------------------------------------------------------------------------------------------------------------------------------------------------

