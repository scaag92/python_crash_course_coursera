"""
STRING METHODS

Python offers a variety of string methods that can be incredibly useful for manipulating and working with text. Here are some commonly used string 
methods along with examples for each:

"""
#---------------------------------------------------------------------------------------------------------------------------------------------------

""" 

- upper(): Converts all characters in the string to uppercase.

"""

text = "hello world"
print(text.upper())  # Output: "HELLO WORLD"

#---------------------------------------------------------------------------------------------------------------------------------------------------

"""

- lower(): Converts all characters in the string to lowercase.

"""

text = "Hello World"
print(text.lower())  # Output: "hello world"

#---------------------------------------------------------------------------------------------------------------------------------------------------
"""

- capitalize(): Capitalizes the first letter of the string.

"""

text = "hello world"
print(text.capitalize())  # Output: "Hello world"

#---------------------------------------------------------------------------------------------------------------------------------------------------
"""

- title(): Capitalizes the first letter of each word in the string.

"""

text = "hello world"
print(text.title())  # Output: "Hello World"

#---------------------------------------------------------------------------------------------------------------------------------------------------
"""

- strip(): Removes any leading and trailing whitespaces or specified characters.

"""

text = "   hello world   "
print(text.strip())  # Output: "hello world"

#---------------------------------------------------------------------------------------------------------------------------------------------------
"""

- split(): Splits the string into a list, using a specified separator (defaults to whitespace).

"""

text = "hello world"
print(text.split())  # Output: ['hello', 'world']

#---------------------------------------------------------------------------------------------------------------------------------------------------
"""

- join(): Joins the elements of an iterable (like a list) into a string, separated by the string it's called on.

"""

words = ["hello", "world"]
print(" ".join(words))  # Output: "hello world"

#---------------------------------------------------------------------------------------------------------------------------------------------------
"""

- replace(): Replaces a specified substring with another substring.

"""

text = "hello world"
print(text.replace("world", "Python"))  # Output: "hello Python"

#---------------------------------------------------------------------------------------------------------------------------------------------------
"""

- find(): Returns the lowest index of a substring (if found). Returns -1 if not found.

"""

text = "hello world"
print(text.find("world"))  # Output: 6

#---------------------------------------------------------------------------------------------------------------------------------------------------
"""

- startswith(): Returns True if the string starts with the specified value.

"""

text = "hello world"
print(text.startswith("hello"))  # Output: True

#---------------------------------------------------------------------------------------------------------------------------------------------------
"""

- isdigit(): Returns True if all characters in the string are digits

"""

text = "12345"
print(text.isdigit())  # Output: True

#---------------------------------------------------------------------------------------------------------------------------------------------------
"""

- isalpha(): Returns True if all characters in the string are alphabetic. 

"""

text = "hello"
print(text.isalpha())  # Output: True

#---------------------------------------------------------------------------------------------------------------------------------------------------
"""

- isspace(): Returns True if all characters in the string are whitespace.

"""

text = "   "
print(text.isspace())  # Output: True

#---------------------------------------------------------------------------------------------------------------------------------------------------
"""

- format(): Method in Python is a powerful tool for string formatting. It allows you to insert values into a string with placeholders, making it 
easier to generate dynamic text. Here are some examples to illustrate its usage:

"""

-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  

# 1 - Basic Formatting:

name = "Alice"
message = "Hello, {}!".format(name)
print(message)  # Output: "Hello, Alice!"

-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  

# 2 - Positional Arguments:

first_name = "Alice"
last_name = "Smith"
message = "Hello, {} {}".format(first_name, last_name)
print(message)  # Output: "Hello, Alice Smith"

-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  

# 3 - Keyword Arguments:

message = "Hello, {first_name} {last_name}".format(first_name="Alice", last_name="Smith")
print(message)  # Output: "Hello, Alice Smith"

-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  

# 4 - Formatting Numbers:

pi = 3.14159
message = "The value of pi is {:.2f}".format(pi)
print(message)  # Output: "The value of pi is 3.14"

-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  

# 5 - Padding and Aligning Strings:

text = "Python"
message = "|{:<10}|".format(text)  # Left align
print(message)  # Output: "|Python    |"

message = "|{:>10}|".format(text)  # Right align
print(message)  # Output: "|    Python|"

message = "|{:^10}|".format(text)  # Center align
print(message)  # Output: "|  Python  |"

-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  

# 6 - Named Placeholders:

data = {'first': 'Alice', 'last': 'Smith'}
message = "Hello, {first} {last}".format(**data)
print(message)  # Output: "Hello, Alice Smith"

-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  

# 7 - Format with Lists:

list_items = ['apples', 'bananas', 'grapes']
message = "I have {}, {} and {}.".format(*list_items)
print(message)  # Output: "I have apples, bananas and grapes."

-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  

# 8 - Mixing Placeholders:

name = "Alice"
age = 30
message = "{0} is {1} years old. {0} loves Python.".format(name, age)
print(message)  # Output: "Alice is 30 years old. Alice loves Python."

#---------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------------------






