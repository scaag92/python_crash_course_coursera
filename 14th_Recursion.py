##################################################################
##################################################################

for left in range(7):
  for right in range(left, 7):
    print("[" + str(left) + "|" + str(right) + "]", end = " ")
  print()

##################################################################
##################################################################

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

##################################################################
##################################################################

def validate_users(users):
  for user in users:
    if is_valid(user):
      print(user + " is valid")
    else:
      print(user + " is invalid")

#validate_users("purplecat")
validate_users(['taylor', 'luisa', 'jamaal'])

##################################################################
##################################################################

def factorial(n):
    result = 1
    for x in range(1,n):
        result = x * result
    return result

for n in range(0,10):
    print(n, factorial(n+1))

##################################################################
##################################################################

for i in range(1,11):
  print(i**3)

##################################################################
##################################################################

for i in range(0,100):
  if i % 7 == 0:
    print(i)

##################################################################
##################################################################

number = 1
while number < 8:
	print(number, end=" ")
	number +=1

##################################################################
##################################################################

def show_letters(word):
	for letter in word:
		print(letter)

show_letters("Hello")
# Should print one line per letter

##################################################################
##################################################################

def digits(n):
	count = 0
	if n == 0:
	  return 1
	while (n != 0):
		count += 1
		n = n // 10 
	return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

##################################################################
##################################################################

def multiplication_table(start, stop):
	for x in range(start,stop+1):
		for y in range(start,stop+1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)

# Should print the multiplication table shown above

" 
1 2 3 
2 4 6 
3 6 9 
"

##################################################################
##################################################################

def counter(start, stop):
    x = start
    if start > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string += str(x)
            if x > stop:
                return_string += ","
            x -= 1
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x < stop:
                return_string += ","
            x += 1
    return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

##################################################################
##################################################################

def even_numbers(maximum):
    return_string = ""
    for x in range(1, maximum):
        if x % 2 == 0:
            return_string += str(x) + " "
    return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

##################################################################
##################################################################

def decade_counter():
	while year < 50:
		year += 10
	return year

##################################################################
##################################################################

for x in range(1, 10, 3):
    print(x)


##################################################################
##################################################################

for x in range(10):
    for y in range(x):
        print(y)

##################################################################
##################################################################


##################################################################
##################################################################


##################################################################
##################################################################


