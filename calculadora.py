#This program will receive two numbers and an operator and will return the result of the operation
#The program will also check if the input is valid
#The program will also check if the operator is valid
#The program will also check if the numbers are valid
#The program will also check if the division by zero is attempted
#The program will also check if the operator is valid

#This function will check if the input is valid
def check_input(input):
    if input.isnumeric():
        return True
    else:
        return False

#This function will check if the operator is valid
def check_operator(operator):
    if operator == '+' or operator == '-' or operator == '*' or operator == '/':
        return True
    else:
        return False

#This function will check if the numbers are valid
def check_numbers(number1, number2):
    if number1.isnumeric() and number2.isnumeric():
        return True
    else:
        return False

#This function will check if the division by zero is attempted
def check_division_by_zero(operator, number2):
    if operator == '/' and number2 == '0':
        return True
    else:
        return False

#This function will check if the operator is valid
def check_operator(operator):
    if operator == '+' or operator == '-' or operator == '*' or operator == '/':
        return True
    else:
        return False

#This function will perform the operation
def calculate(number1, number2, operator):
    if operator == '+':
        return int(number1) + int(number2)
    if operator == '-':
        return int(number1) - int(number2)
    if operator == '*':
        return int(number1) * int(number2)
    if operator == '/':
        return int(number1) / int(number2)

#This function will print the result
def print_result(result):
    print('The result is: ', result)

#This function will print the error message
def print_error_message():
    print('Invalid input')

#This function will print the error message
def print_error_message_operator():
    print('Invalid operator')

#This function will print the error message
def print_error_message_numbers():
    print('Invalid numbers')

#This function will print the error message
def print_error_message_division_by_zero():
    print('Division by zero is not allowed')

#This function will print the error message
def print_error_message_operator():
    print('Invalid operator')

#This function will print the error message
def print_error_message_operator():
    print('Invalid operator')

#This function will receive the input
def get_input():
    number1 = input('Enter the first number: ')
    number2 = input('Enter the second number: ')
    operator = input('Enter the operator: ')
    return number1, number2, operator

#This function will call the other functions
def main():
    number1, number2, operator = get_input()
    if check_input(number1) and check_input(number2) and check_operator(operator) and check_numbers(number1, number2) and not check_division_by_zero(operator, number2):
        result = calculate(number1, number2, operator)
        print_result(result)
    else:
        if not check_input(number1) or not check_input(number2):
            print_error_message()
        if not check_operator(operator):
            print_error_message_operator()
        if not check_numbers(number1, number2):
            print_error_message_numbers()
        if check_division_by_zero(operator, number2):
            print_error_message_division_by_zero()

#This will call the main function
main()




