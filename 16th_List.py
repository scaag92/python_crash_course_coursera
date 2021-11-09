##################################################################
##################################################################

# List-specific operations and methods
list[i] = x # Replaces the element at index i with x
list.append(x) #Inserts x at the end of the list
list.insert(i, x) #Inserts x at index i
list.pop(i) # Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.
list.remove(x) # Removes the first occurrence of x in the list
list.sort() # Sorts the items in the list
list.reverse() # Reverses the order of items of the list
list.clear() # Removes all the items of the list
list.copy() # Creates a copy of the list
list.extend(other_list) #Appends all the elements of other_list at the end of list

##################################################################
##################################################################
def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing

##################################################################
##################################################################

def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0

    # Iterate through the list
    for element in elements:
        # Does this element belong in the resulting list?
        if i < len(elements):
            # Add this element to the resulting list
            new_list.append(elements[i])
        # Increment i
        i += 2

    return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

##################################################################
##################################################################


