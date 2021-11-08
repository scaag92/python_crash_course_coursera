def format_address(address_string):
    # Declare variables
    # Separate the address string into parts
    address_string = address_string.split()
    # Traverse through the address parts
    for add in address_string:
    # Determine if the address part is the
    # house number or part of the street name
        if add.isnumeric() == True:
            num = add


    # Does anything else need to be done
    # before returning the result?

    i = address_string.index(num)
    add_name = address_string[i+1:]
    add_name = " ".join(add_name)

# Return the formatted string

    return "house number {num} on street named {add_name}".format(num=num,add_name=add_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"