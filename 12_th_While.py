####################################################################################
####################################################################################

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(10)

####################################################################################
####################################################################################

def count_down(start_number):
  current = start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)

####################################################################################
####################################################################################

def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n += 1
print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 

####################################################################################
####################################################################################

def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor+=1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT

####################################################################################
####################################################################################

def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  i = n
  while n % 2 == 0 and i > 0:
    n = n / 2
    i -= 1
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False


####################################################################################
####################################################################################

def sum_divisors(n):
    i = 1
    suma = 0
    modi = 0
    while i < n:
      modi = n % i
      if modi == 0:
        suma = suma + i
      i += 1
    return suma
# print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51

####################################################################################
####################################################################################

def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = multiplier * number 
		# What is the additional condition to exit out of the loop?
		if result % number != 0 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1
	

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24

####################################################################################
####################################################################################

# This function counts the number of integer factors for a
# "given_number" variable, passed through the function’s parameters.
# The "count" return value includes the "given_number" itself as a
# factor (n*1).
def count_factors(given_number):

  # To include the "given_number" variable as a "factor", initialize
  # the "factor" variable with the value 1 (if the "factor" variable
  # were to start at 2, the "given_number" itself would be excluded).
  factor = 1
  count = 1

  # This "if" block will run if the "given_number" equals 0.
  if given_number == 0:
    # If True, the return value will be 0 factors.
    return 0

  # The while loop will run while the "factor" is still less than
  # the "given_number" variable.
  while factor < given_number:
    # This "if" block checks if the "given_number" can be divided by
    # the "factor" variable without leaving a remainder. The modulo
    # operator % is used to test for a remainder.
    if given_number % factor == 0:
      # If True, then the "factor" variable is added to the count of
      # the "given_number"’s integer factors.
      count += 1
    # When exiting the if block, increment the "factor" variable by 1
    # to divide the "given_number" variable by a new "factor" value
    # inside the while loop.
    factor += 1

  # When the interpreter exits either the while loop or the top if
  # block, it will return the value of the "count" variable.
  return count

print(count_factors(0)) # Count value will be 0
print(count_factors(3)) # Should count 2 factors (1x3)
print(count_factors(10)) # Should count 4 factors (1x10, 2x5)
print(count_factors(24)) # Should count 8 factors (1x24, 2x12, 3x8,
# and 4x6).

####################################################################################
####################################################################################

# This function outputs an addition table. It is written to end after
# printing 5 lines of the addition table, but it will break out of the
# loop if the "my_sum" variable exceeds 20. 
 
# The function accepts a "given_number" variable through its 
# parameters.
def addition_table(given_number):
 
    # The "iterated_number" and "my_sum" variables are initialized with
    # the value of 1. Although the "my_sum" variable does not need any
    # specific initial value, it still must be assigned a data type
    # before being used in the while loop. By initializing "my_sum"
    # with any integer, the data type will be set to int.
    iterated_number = 1
    my_sum = 1
 
    # The while loop will run while it is True that the   
    # "iterated_number" is less than or equal to 5.
    while iterated_number <= 5:
 
        # The "my_sum" variable is assigned the value of the
        # "given_number" plus the "iterated_number" variables.
        my_sum = given_number + iterated_number
 
        # Test to see if the "my_sum" variable is greater than 20.
        if my_sum > 20:
            # If True, then use the break keyword to exit the loop. 
            break
        # If False, the Python interpreter will move to the next line 
        # in the while loop after the if-statement has ended.  
 
        # The print function will output the "given_number" plus
        # the "iterated_number" equals "my_sum".
        print(str(given_number), "+", str(iterated_number), "=", str(my_sum))
 
        # Increment the "iterated_number" before the while loop starts
        # over again to print a new "my_sum" value.
        iterated_number += 1
 
 
addition_table(5)
addition_table(17)
addition_table(30)

# Expected output:
# 5 + 1 = 6
# 5 + 2 = 7
# 5 + 3 = 8
# 5 + 4 = 9
# 5 + 5 = 10
# 17 + 1 = 18
# 17 + 2 = 19
# 17 + 3 = 20
# None


####################################################################################
####################################################################################

def is_power_of_two(number):
  # This while loop checks if the "number" can be divided by two
  # without leaving a remainder. How can you change the while loop to
  # avoid a Python ZeroDivisionError?
  while number > 1 or number % 2 == 0:
  # If after dividing by 2 "number" equals 1, then "number" is a power
  # of 2.
    number = number / 2
    if number != 1:
      return  True
    else:
      return False

  return True

# Calls to the function
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

####################################################################################
####################################################################################

# Fill in the blanks so that the while loop continues to run while the
# "divisor" variable is less than the "number" parameter.

def sum_divisors(number):
# Initialize the appropriate variables
  divisor = 1
  total = 0

  # Avoid dividing by 0 and negative numbers
  # in the while loop by exiting the function
  # if "number" is less than one
  if number < 1:
    return 0

  # Complete the while loop
  while divisor < number:
    if number % divisor == 0:
      total += divisor
    # Increment the correct variable
    divisor += 1

  # Return the correct variable
  return total


print(sum_divisors(0)) # Should print 0
print(sum_divisors(3)) # Should print 1
# 1
print(sum_divisors(36)) # Should print 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should print 1+2+3+6+17+34+51
# 114

####################################################################################
####################################################################################

def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        if  result > 25 :
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

multiplication_table(5)
# Should print:
# 5x1=5
# 5x2=10
# 5x3=15
# 5x4=20
# 5x5=25

multiplication_table(8)
# Should print:
# 8x1=8
# 8x2=16
# 8x3=24

####################################################################################
####################################################################################

def multiplication_table(start, stop):
    # Complete the outer loop range
    for x in range(start,stop+1):
         # Complete the inner loop range
        for y in range(start,stop+1):
            # Prints the value of "x" multiplied by "y"
            # and inserts a space after each value
            print(str(x*y), end=" ")
        # An empty print() function inserts a line break at the
        # end of the row
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above

####################################################################################
####################################################################################

def countdown(start):
    x = start
    if x > 0:
        return_string = "Counting down to 0: "
        while x <= start and x >= 0: # Complete the while loop
            return_string += str(x)  # Add the numbers to the "return_string"
            if x > 0:
                return_string += ","
            x -= 1 # Decrement the appropriate variable
    else:
        return_string = "Cannot count down to 0"
    return return_string


print(countdown(10)) # Should be "Counting down to 0: 10,9,8,7,6,5,4,3,2,1,0"
print(countdown(2)) # Should be "Counting down to 0: 2,1,0"
print(countdown(0)) # Should be "Cannot count down to 0"

####################################################################################
####################################################################################



