#---------------------------------------------------------------------------------------------------------------------------------------------------
"""

8th PYTHON FUNCTIONS

Functions in Python are defined using the def keyword and are used to encapsulate reusable pieces of code. They can take arguments, perform 
operations, and return results. Here are some examples to illustrate how functions are created and used in Python:

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------

# Function with Parameters

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Prints "Hello, Alice!"

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Function with Return Value

def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # Prints 7


#---------------------------------------------------------------------------------------------------------------------------------------------------

# Default Parameter Values

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Bob")                   # Prints "Hello, Bob!"
greet("Bob", greeting="Hi")    # Prints "Hi, Bob!"

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Arbitrary Number of Arguments

def sum_all(*args):
    return sum(args)

result = sum_all(1, 2, 3, 4)
print(result)  # Prints 10

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Keyword Arguments

def greet(**kwargs):
    name = kwargs.get('name', 'there')
    greeting = kwargs.get('greeting', 'Hello')
    print(f"{greeting}, {name}!")

greet(name="Alice", greeting="Hi")  # Prints "Hi, Alice!"
greet()                             # Prints "Hello, there!"


#---------------------------------------------------------------------------------------------------------------------------------------------------

# Docstrings

def add(a, b):
    """
    Adds two numbers and returns the result.
    
    Parameters:
    a (int): The first number
    b (int): The second number
    
    Returns:
    int: The sum of a and b
    """
    return a + b

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Nested Functions

def outer_function(text):
    def inner_function():
        return text.upper()
    return inner_function()

result = outer_function("hello")
print(result)  # Prints "HELLO"


#---------------------------------------------------------------------------------------------------------------------------------------------------

# Lambda Functions

multiply = lambda x, y: x * y

result = multiply(2, 3)
print(result)  # Prints 6

#---------------------------------------------------------------------------------------------------------------------------------------------------


def test(name):
    print(name)

test("hola")

#---------------------------------------------------------------------------------------------------------------------------------------------------


def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)

#---------------------------------------------------------------------------------------------------------------------------------------------------


def month_days(month, days):
    print( str(month) + " has " + str(days) + " days.")

month_days("June",30)
month_days("July",31)

#---------------------------------------------------------------------------------------------------------------------------------------------------


def rectangle_area(base, height):
	area = base * height  # the area is base*height
	print("The area is " + str(area))
rectangle_area(5,6)

#---------------------------------------------------------------------------------------------------------------------------------------------------

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(my_trip_km*2))

#---------------------------------------------------------------------------------------------------------------------------------------------------


# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

#---------------------------------------------------------------------------------------------------------------------------------------------------

def lucky_number(name):
  number = len(name) * 9
  message = "Hello " + name + ". Your lucky number is " + str(number)
  return message
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))

#---------------------------------------------------------------------------------------------------------------------------------------------------




