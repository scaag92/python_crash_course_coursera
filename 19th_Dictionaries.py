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




##################################################################
##################################################################

