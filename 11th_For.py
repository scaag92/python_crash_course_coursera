####################################################################################
####################################################################################

def square(n):
    return n*n

def sum_squares(x):
    suma = 0
    for n in range(x):
        suma += square(n)
    return suma

print(sum_squares(10)) # Should be 285

####################################################################################
####################################################################################

values= [ 23, 52, 59, 37, 48]
suma = 0 
length = 0
for value in values:
    suma += 1
    length = 0 
print("Total sum: " + str(suma) + "- Average: " + str(suma/length))

####################################################################################
####################################################################################

def factorial(n):
    result = 1  
    for i in range(1, n + 1):
        result = i * result
        i += 1

    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

####################################################################################
####################################################################################

def to_celsius(x):
    return (x-32)*5/9

for x in range (0,100,10):
    print(x, to_celsius(x))


####################################################################################
####################################################################################

def odd_numbers(maximum):
    
    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all 
    # odd numbers up to and including the "maximum" value.
    for i in range(0,maximum+1):
        # Complete the body of the loop by appending the odd number
        # followed by a space to the "return_string" variable.
        if i % 2 != 0:
           return_string += str(i) + " "  

    # This .strip command will remove the final " " space 
    # at the end of the "return_string".
    return return_string.strip()


print(odd_numbers(6))  # Should be 1 3 5
print(odd_numbers(10)) # Should be 1 3 5 7 9
print(odd_numbers(1))  # Should be 1
print(odd_numbers(3))  # Should be 1 3
print(odd_numbers(0))  # No numbers displayed

####################################################################################
####################################################################################









####################################################################################
####################################################################################
