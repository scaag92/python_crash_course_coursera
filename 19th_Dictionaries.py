###################################################################
###################################################################

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24  # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc) # Is there a Chapter 5?
del toc["Epilogue"]

##################################################################
##################################################################

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
    print(extension)

for key, value in file_counts.items():
    print("The format is: {} and the value is {} ".format(key,value))

for val in file_counts.values():
    print(val)

for k in file_counts.keys():
    print(k)

##################################################################
##################################################################

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("Cristian Arturo Arias Guerrero".lower()))

##################################################################
##################################################################


x = {"Sun":23,"Moon":32,"Mars":64}
y = {"Soccer":90,"Basketball":87,"Voleyball":60}
print(x)
print("_________________________\n")
print(len(x))
print("_________________________\n")
for items in x:
    print(items)
print("_________________________\n")
for planet, id in x.items():
    print(planet)
print("_________________________\n")
print(x["Sun"])
print("_________________________\n")
x.keys()
print("_________________________\n")
x.values()
print("_________________________\n")
print(x)
x.update(y)
print(y)
print(y)
print("_________________________\n")
y.clear()
print(y)


##################################################################
##################################################################

def email_list(domains):
    emails = []
    for domain in domains:
        print(domain)
        for x in domains[domain]:
            emails.append(x + "@" + domain)
    return (emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

#Should return as email:  diana.prince@gmail.com.

##################################################################
##################################################################

def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for fruit, value in basket.items():
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?
        print(value)
        total = value + total
    # Limit the return value to 2 decimal places
    return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
             "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44

##################################################################
##################################################################

def email_list(domains):
    emails = []
    for domain in domains:
        for user in domains[domain]:
            emails.append(user + "@" + domain)
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

##################################################################
##################################################################

def groups_per_user(group_dictionary):
    user_groups = {}
    for group, users in group_dictionary.items():
        for user in users:
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)
    return user_groups

print(groups_per_user({"local": ["admin", "userA"],
                       "public":  ["admin", "userB"],
                       "administrator": ["admin"] }))


##################################################################
##################################################################

def count_letters(text):
    result = {}
    value = 0
    # Go through each letter in the text
    text = text.lower()
    for letter in text:
        # Check if the letter needs to be counted or not
        if letter.isalpha() == True:
            result[letter] = value
        # Add or increment the value in the dictionary
    for letter in text:
        if letter in result:
            result[letter] += 1
    return result

print(count_letters("AaBbCc"))
## Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

##################################################################
##################################################################

def combine_guests(guests1, guests2):
    # Combine both dictionaries into one, with each key listed
    # only once, and the value from guests1 taking precedence
    result = {}
    result.update(guests2)
    result.update(guests1)
    return result


Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

##################################################################
##################################################################

def car_listing(car_prices):
    result = ""
    for model, price in car_prices.items():
        result += "{model} costs {price} dollars".format(model=model, price=price) + "\n"
    return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

##################################################################
##################################################################

def squares(start, end):
    list = []

    for i in range (start,end+1):
        list.append(i*i)

    return list

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

##################################################################
##################################################################

def combine_lists(list1, list2):
    # Generate a new list containing the elements of list2
    # Followed by the elements of list1 in reverse order
    list1.reverse()
    list2.reverse()
    list2 = list2 + list1
    return list2

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

##################################################################
##################################################################

def highlight_word(sentence, word):
    sentence = sentence.replace("!","")
    sentence = sentence.split()
    result = []
    for senten in sentence:
        if senten == word:
            result.append(senten.upper())
        else:
            result.append(senten)
    return(" ".join(result))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

##################################################################
##################################################################

