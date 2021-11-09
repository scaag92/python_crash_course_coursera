##################################################################
##################################################################

#List Comprehension

multiples = []
for x in range(1,11):
    multiples.append(x*7)
print(multiples)

##################################################################
##################################################################

multi = [x*7 for x in range(1,11)]
print(multi)

##################################################################
##################################################################

languages = ["Python","Perl","Ruby","Go","Java"]
lenghts = [len(language) for language in languages]
print(lenghts)

##################################################################
##################################################################

z = [x for x in range(0,101) if x % 3 == 0]
print(z)

##################################################################
##################################################################

def odd_numbers(n):
    return [x for x in range(1, n + 1) if x %2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10))  # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11))  # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1))  # Should print []

##################################################################
##################################################################

l = [r*2 for r in range(1,11)]
print(l)

##################################################################
##################################################################

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [filename[:-2]  if ".hpp" in filename else filename for filename in filenames ]

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

##################################################################
##################################################################

def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        say = say + word[1:] + word[0] + "ay" + " "
        # Turn the list back into a phrase
    return say

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

##################################################################
##################################################################

def group_list(group, users):
    members = group + ": " + ", ".join(users)
    return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"


##################################################################
##################################################################

def guest_list(guests):
    for guest in guests:
        name , age , role = guest
        print("{name} is {age} years old and works as {role}".format(name=name, age=age, role=role))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
 """
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""

##################################################################
##################################################################

