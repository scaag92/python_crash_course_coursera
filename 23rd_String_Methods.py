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
