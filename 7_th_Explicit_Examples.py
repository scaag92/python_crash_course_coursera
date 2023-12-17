#---------------------------------------------------------------------------------------------------------------------------------------------------

"""

7th Explicit Examples


"""
#---------------------------------------------------------------------------------------------------------------------------------------------------


numerator = int(input())
denominator = int(input())
result = numerator / denominator
str(result)
print(result)

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Converting to Integer (int())

num_float = 3.14
num_str = "10"

int_from_float = int(num_float)  # 3
int_from_str = int(num_str)      # 10

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Converting to Float (float())

num_str = "3.14"
num_int = 5

float_from_str = float(num_str)  # 3.14
float_from_int = float(num_int)  # 5.0

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Converting to String (str())

num = 10
boolean = True

str_from_num = str(num)      # "10"
str_from_bool = str(boolean) # "True"

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Converting to List (list())

tuple_data = (1, 2, 3)
str_data = "hello"

list_from_tuple = list(tuple_data)  # [1, 2, 3]
list_from_str = list(str_data)      # ['h', 'e', 'l', 'l', 'o']

#---------------------------------------------------------------------------------------------------------------------------------------------------

# Converting to Tuple (tuple())

list_data = [1, 2, 3]
str_data = "hello"

tuple_from_list = tuple(list_data)  # (1, 2, 3)
tuple_from_str = tuple(str_data)    # ('h', 'e', 'l', 'l', 'o')


#---------------------------------------------------------------------------------------------------------------------------------------------------

# Converting to Dictionary (dict())

pair_list = [("a", 1), ("b", 2), ("c", 3)]

dict_from_pairs = dict(pair_list)  # {'a': 1, 'b': 2, 'c': 3}

#---------------------------------------------------------------------------------------------------------------------------------------------------

"""

Notes on Explicit Conversion
Error Handling: Type conversion can fail if the value is not compatible with the target type, potentially raising a ValueError or TypeError.
Loss of Information: Converting from a more precise to a less precise data type (like float to int) may result in loss of information.
Immutable Types: Converting mutable types (like lists) to immutable types (like tuples) creates a completely new object.
Explicit type conversions are essential for achieving desired data types and formats, especially when dealing with user input or data from external 
sources.

"""

#---------------------------------------------------------------------------------------------------------------------------------------------------





