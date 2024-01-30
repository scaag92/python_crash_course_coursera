#---------------------------------------------------------------------------------------------------------------------------------------------------

"""
Object Oriented Programing


As a Python developer, understanding Object-Oriented Programming (OOP) is crucial. OOP in Python allows you to structure your code by bundling 
related properties and behaviors into individual objects. This concept revolves around classes and objects, along with concepts like inheritance, 
encapsulation, and polymorphism.

The attributes are the characteristics associated to a type
The methods are the functions associated to a type

In object-oriented programming, concepts are modeled as classes and objects. An idea is defined using a class, and an instance of this class is called
an object. Almost everything in Python is an object, including strings, lists, dictionaries, and numbers. When we create a list in Python, we’re 
creating an object which is an instance of the list class, which represents the concept of a list. Classes also have attributes and methods associated 
with them. Attributes are the characteristics of the class, while methods are functions that are part of the class.

Key Concepts of OOP:
Class: A blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class can use.
Object: An instance of a class. Each object can have its own attributes and methods.
Inheritance: A way to form new classes using classes that have already been defined.
Encapsulation: Hiding the private details of a class from other objects.
Polymorphism: A way to use a single type entity (method, operator, or object) to represent different types in different scenarios.

"""

#---------------------------------------------------------------------------------------------------------------------------------------------------

"""

Classes

We can create and define our classes in Python similar to how we define functions. We start with the class keyword, followed by the name of our 
class and a colon. Python style guidelines recommend class names to start with a capital letter. After the class definition line is the class body,
indented to the right. Inside the class body, we can define attributes for the class.

We can use the type() function to figure out what class a variable or value belongs to. For example, type(" ") tells us that this is a string class.
The only attribute in this case is the string value, but there are a bunch of methods associated with the class. We've seen the upper() method, which 
returns the string in all uppercase, as well as isnumeric() which returns a boolean telling us whether or not the string is a number. You can use 
the dir() function to print all the attributes and methods of an object. Each string is an instance of the string class, having the same methods of 
the parent class. Since the content of the string is different, the methods will return different values. You can also use the help() function on an 
object, which will return the documentation for the corresponding class. This will show all the methods for the class, along with parameters the 
methods receive, types of return values, and a description of the methods.

"""
type(0)

dir("")
# Tell us all the methods associated with a dir class

help("")
# Give us all the information related to this class. In this case string class.


#---------------------------------------------------------------------------------------------------------------------------------------------------
"""

Name of the class must begin with a capital letter
Dot notation
Lets us to access any of the abilities the object might have (Called methods) or information ir might store (Called attributes)


"""

# Creating a Python Class
class Apple:
	color = ""
	flavor = ""

#Instancing the class
jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"


print(jonagold.flavor)
print(jonagold.flavor.upper())

#---------------------------------------------------------------------------------------------------------------------------------------------------

class Flower:
  color = 'unknown'

rose = Flower()
rose.color = 'red'

violet = Flower()
violet.color = 'blue'
this_pun_is_for_you = "Color Flowers are: {} and {}".format(rose.color, violet.color)

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you)

#---------------------------------------------------------------------------------------------------------------------------------------------------

# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	return_city = " "
	if city1.population > min_population and city1.population < city2.population:
		if city1.elevation > city2.elevation and city1.elevation > city3.elevation:
			return_city = ("{}, {}".format(city1.name, city1.country))
			return return_city

	if city2.population > min_population and city2.population < city3.population:
		return_city = ("{}, {}".format(city2.name, city2.country))
		return return_city

	if city3.population > min_population:
		return_city = ("{}, {}".format(city3.name, city3.country))
		return return_city

	else:
		return ""
print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""


#---------------------------------------------------------------------------------------------------------------------------------------------------

# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0


johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1


def exchange_apples(you, me):
    # Here, despite G.B. Shaw's quote, our characters have started with       #different amounts of apples so we can better observe the results.
    # We're going to have Martin and Johanna exchange ALL their apples with #one another.
    # Hint: how would you switch values of variables,
    # so that "you" and "me" will exchange ALL their apples with one another?
    # Do you need a temporary variable to store one of the values?
    # You may need more than one line of code to do that, which is OK.
    tem = you.apples
    you.apples = me.apples
    me.apples = tem
    return you.apples, me.apples


def exchange_ideas(you, me):
    # "you" and "me" will share our ideas with one another.
    # What operations need to be performed, so that each object receives
    # the shared number of ideas?
    # Hint: how would you assign the total number of ideas to
    # each idea attribute? Do you need a temporary variable to store
    # the sum of ideas, or can you find another way?
    # Use as many lines of code as you need here.
    tem = you.ideas
    you.ideas += me.ideas
    me.ideas += tem

    return you.ideas, me.ideas


exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))

#---------------------------------------------------------------------------------------------------------------------------------------------------

class Furniture:
	color = ""
	material = ""

table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table))
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch))
# Should be "This piece of furniture is made of red leather"

#---------------------------------------------------------------------------------------------------------------------------------------------------

class Dog:
  years = 0
  def dog_years(self):
    return self.years * 7

fido=Dog()
fido.years=3
print(fido.dog_years())

#---------------------------------------------------------------------------------------------------------------------------------------------------

"""

CONSTRUCTOR METHOD - SPECIAL METHODS

Instead of creating classes with empty or default values, we can set these values when we create the instance. This ensures that we don't miss an 
important value and avoids a lot of unnecessary lines of code. To do this, we use a special method called a constructor. Below is an example of 
an Apple class with a constructor method defined.

When you call the name of a class, the constructor of that class is called. This constructor method is always named __init__. You might remember
that special methods start and end with two underscore characters.

"""

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is " + str(self.name)

# Create a new instance with a name of your choice
some_person = Person("Cristian")
# Call the greeting method
print(some_person.greeting())

#---------------------------------------------------------------------------------------------------------------------------------------------------

"""

In addition to the __init__ constructor special method, there is also the __str__ special method. This method allows us to define how an instance of an 
object will be printed when it’s passed to the print() function. If an object doesn’t have this special method defined, it will wind up using the default 
representation, which will print the position of the object in memory. Not super useful. Here is our Apple class, with the __str__ method added:

"""

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

jonagold = Apple("red", "sweet")
print(jonagold)

# This apple is red and its flavor is sweet

#---------------------------------------------------------------------------------------------------------------------------------------------------

"""
DOCUMENTATION WITH DOCSTRINGS:

The Python help function can be super helpful for easily pulling up documentation for classes and methods. We can call the help function on one of 
our classes, which will return some basic info about the methods defined in our class:

"""
class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    """ Outputs a message with the name of the person """
    print("Hello! My name is {name}.".format(name=self.name)) 

help(Person)

#---------------------------------------------------------------------------------------------------------------------------------------------------

class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))

class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()

