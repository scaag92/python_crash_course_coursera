##################################################################
##################################################################

def file_size(file_info):
	name, tipe, size= file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21


##################################################################
##################################################################

animals = ["Lion","Zebra","Dolphin","Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Toal characters: {}, Average length: {}".format(chars,chars/len(animals)))

##################################################################
##################################################################

winners = ["Ashley","Dylan","Resse"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person ))

##################################################################
##################################################################

def skip_elements(elements):
    # code goes here
    result = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            result.append(element)
    return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

##################################################################
##################################################################

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(people, name))
    return result

print(full_emails([("alex@example.com", "Alex Diego"),("shay@example.com", "Shay Brandt")]))

##################################################################
##################################################################


def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    #Iterating over each digit in octal
    for digit in [int(n) for n in str(octal)]:

        #Checking for each of permission values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
            else:
                result += "-"
    return result

print(octal_to_string(755))


##################################################################
##################################################################