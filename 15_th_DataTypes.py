##################################################################
##################################################################



def double_word(word):
    word = word * 2 + str(len(word * 2))
    return word

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

##################################################################
##################################################################

def first_and_last(message):
    if message == "":
        return True
    elif message[0] == message[-1]:
       return True
    else:     
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

##################################################################
##################################################################

word = "supercalifragilisticexpialidocious"
print(word.index('x'))

##################################################################
##################################################################

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

##################################################################
##################################################################

def initials(phrase):
    words = phrase.split()
    print(words)
    result = ""
    for word in words:
        result += word[0]
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

##################################################################
##################################################################

index() #Is used to find a character or word inside the string
upper() #This will conver the string into uppercase letters
lower() #This will conver the string into lowercase letters
strip() #Removes surronding spaces
lstrip() #Remove spaces on the left
rstrip() #Remove spaces on the right
count() #Return how many time are a character or word inside a sentence
endswith() #Return if 
isnumeric()
join() #Is used for concatenate
	Ex: 	" ".join(["This","is","a","Sentence"])
	Result: This is a sentence
split() #Is used to split a sentence into a list

-----------------------------------------------------------------

string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
string.count(substring) Returns the number of times substring is present in the string
string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter 

##################################################################
##################################################################

name = "Manny"
number = len(name) * 3
print("Hello {}, You're lucky number is: {}".format(name,number))
print("Hello {name}, You're lucky nummer is {number}".format(name=name,number=len(number)*3))

##################################################################
##################################################################

def student_grade(name, grade):
	return "{name} received {grade}% on the exam".format(name=name,grade=grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

##################################################################
##################################################################

price=7.5
with_taxes=price * 1.09
print(price,with_taxes)
price("Base price is: ${:.2f}. With Tax:${:.2f}".format(price,with_taxes))

##################################################################
##################################################################

def to_celsius(x):
    return (x-32)*5/9

for x in range(0,100,10):
    print("{:>5} F  | {:>6.2f} C".format(x, to_celsius(x)))

##################################################################
##################################################################

def is_palindrome(input_string):
    # We'll create two strings, to compare them
    new_string = ""
    reverse_string = ""
    # Traverse through each letter of the input string
    for i in input_string:
        # Add any non-blank letters to the
        # end of one string, and to the front
        # of the other string.
        if i == " ":
            new_string = i + new_string
            reverse_string = reverse_string + i
        else:
            new_string = new_string + i
            reverse_string = i + reverse_string

    if new_string.lower().strip() == reverse_string.lower().strip():
        return True
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

##################################################################

def convert_distance(miles):
    km = miles * 1.6
    result = "{miles} miles equals {km:.1f} km".format(miles=miles,km=km)
    return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

##################################################################

def nametag(first_name, last_name):
    return("{first}, {last}.".format(first=first_name,last=last_name[:1]))

print(nametag("Jane", "Smith"))
# Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))
# Should display "Jean-Luc G." 

##################################################################




