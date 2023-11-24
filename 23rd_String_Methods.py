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

# 1 - Basic Usage with a String:

text = "Hello, World!"
length = len(text)
print(length)  # Output: 13

-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  

# 2 - String with Spaces:

text = "Python programming"
length = len(text)
print(length)  # Output: 18

-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  

# 3 - Empty String:

text = ""
length = len(text)
print(length)  # Output: 0

-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  

# 4 - String with Newline and Tab Characters:

text = "Line 1\nLine 2\tTab"
length = len(text)
print(length)  # Output: 16

-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  

# 5 - String with Unicode Characters:

text = "こんにちは"  # Japanese for "Hello"
length = len(text)
print(length)  # Output: 5

-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  

# 6 - Length of a Concatenated String:

greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name
length = len(full_greeting)
print(length)  # Output: 12


-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  

# 7 - Multiline String:

text = """First line
Second line
Third line"""
length = len(text)
print(length)  # Output depends on the length of each line and the newline characters

-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  

# 8 - String with Emojis:

text = "Python is fun 🐍"
length = len(text)
print(length)  # Output: 14

#---------------------------------------------------------------------------------------------------------------------------------------------------

# string[x]

word = "casa"
print(word[0]) # w 

#---------------------------------------------------------------------------------------------------------------------------------------------------

# This function accepts a given string and checks each character of
# the string to see if it is a letter or not. If the character is a
# letter, that letter is added to the end of the string variable
# "forwards" and to the beginning of the string variable "backwards".
def mirrored_string(my_string):

    # Two variables are initialized as string data types using empty
    # quotes. The variable "forwards" will hold the "my_string"
    # minus any character that is not a letter. The "backwards"
    # variable will hold the same letters as "forwards", but in
    # in reverse order.
    forwards = ""
    backwards = ""

    # The for loop iterates through each character of the "my_string"
    for character in my_string:

        # The if-statement checks if the character is not a space.
        if character.isalpha():

            # If True, the body of the loop adds the character to the
            # to the end of "forwards" and to the front of
            # "backwards".
            forwards += character
            backwards = character + backwards

        # If False (meaning the character is not a letter), no action
        # is needed. This coding approach results prevents any
        # non-alphabetical characters from being written to the
        # "forwards" and "backwards" variables. The for loop will
        # restart until all characters in "my_string" have been
        # processed.

    # The final if-statement compares the "forwards" and "backwards"
    # strings to see if the letters are the same both forwards and
    # backwards. Since Python is case sensitive, the two strings will
    # need to be converted to use the same case for this comparison.
    if forwards.lower() == backwards.lower():
        return True
    return False

print(mirrored_string("12 Noon")) # Should be True
print(mirrored_string("Was it a car or cat I saw")) # Should be False
print(mirrored_string("'eve, Madam Eve")) # Should be True

#---------------------------------------------------------------------------------------------------------------------------------------------------

# This function converts measurement equivalents. Output is formatted 
# as, "x ounces equals y pounds", with y limited to 2 decimal places. 
def convert_weight(ounces):

    # Conversion formula: 1 pound = 16 ounces
    pounds = ounces/16 
    
    # The result is composed using the .format() method. There are two
    # placeholders in the string: the first is for the "ounces" 
    # variable and the second is for the "pounds" variable. The second
    # placeholder formats the float result of the conversion 
    # calculation to be limited to 2 decimal places.
    result = "{} ounces equals {:.2f} pounds".format(ounces,pounds)
    return result


print(convert_weight(12)) # Should be: 12 ounces equals 0.75 pounds
print(convert_weight(50.5)) # Should be: 50.5 ounces equals 3.16 pounds
print(convert_weight(16)) # Should be: 16 ounces equals 1.00 pounds

#---------------------------------------------------------------------------------------------------------------------------------------------------

# This function generates a username using the first 3 letters of a
# user’s last name plus their birth year. 
def username(last_name, birth_year):
    
    # The .format() method will use the first 3 letters at index 
    # positions [0,1,2] of the "last_name" variable for the first
    # {} placeholder. The second {} placeholder concatenates the user’s
    #  "birth_year" to that string to form a new string username.
    return("{}{}".format(last_name[0:3],birth_year))


print(username("Ivanov", "1985")) 
# Should display "Iva1985" 
print(username("Rodríguez", "2000")) 
# Should display "Rod2000" 
print(username("Deng", "1991")) 
# Should display "Den1991"

#---------------------------------------------------------------------------------------------------------------------------------------------------

# This function checks a given schedule entry for an old date and, if 
# found, the function replaces it with a new date. 
def replace_date(schedule, old_date, new_date):

    # Check if the given "old_date" appears at the end of the given 
    # string variable "schedule". 
    if schedule.endswith(old_date):

        # If True, the body of the if-block will run. The variable "n" is
        # used to hold the slicing index position. The len() function
        # is used to measure the length of the string "new_date".
        p = len(old_date)

        # The "new_schedule" string holds the updated string with the 
        # old date replaced by the new date. The schedule[:-p] part of 
        # the code trims the "old_date" substring from "schedule" 
        # starting at the final index position (or right-side) counting
        # towards the left the same number of index positions as 
        # calculated from len(old_date). Then, the code schedule[-p:]
        # starts the indexing position at the slot where the first
        # character of the "old_date" used to be positioned. The 
        # .replace(old_date, new_date) code inserts the "new_date" into
        # the position where the "old_date" used to exist.  
        new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)

        # Returns the schedule with the new date.
        return new_schedule
        
    # If the schedule does not end with the old date, then return the
    # original sentence without any modifications.
    return schedule
 
 
print(replace_date("Last year’s annual report will be released in March 2023", "2023", "2024")) 
# Should display "Last year’s annual report will be released in March 2024"
print(replace_date("In April, the CEO will hold a conference", "April", "May")) 
# Should display "In April, the CEO will hold a conference"
print(replace_date("The convention is scheduled for October", "October", "June")) 
# Should display "The convention is scheduled for June"

#---------------------------------------------------------------------------------------------------------------------------------------------------
