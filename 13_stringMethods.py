# Strings are immutable in nature and can't be changed therefore, every methods return a new string
name = "Deependra Parmar"
lastname = "parmar"

print("Length of name is: ", len(name))
print("Name in the uppercase is: ", name.upper())
print("Name in the lowercase is: ", name.lower())
print("Name with removed whitespaces: ", name.strip())
print("Name with removed trailing characters: ", name.rstrip('!'))
print("Name with replaced characters: ", name.replace("D","T"))
print("Returning list by splitting with : ", name.split(" "))
print("Capitalize first letter of name: ", lastname.capitalize())
print("Name in the center: ", name.center(50))
print("Count of e in the name is: ", name.count('e'))
print("Whether name ending with mar: ", name.endswith("mar")) # we also have startswith()
print("Whether pen exists in the name: ", name.endswith('pen',0,6))

# index and find are too similar with just one difference. Find if not finds returns -1 while index returns an exception if not found the string or substring
print("First occurence of e in name is: ", name.find('e'))
print("First occurence of e in name is: ", name.index('e'))
print("Is Alphanumerics? ", lastname.isalnum())
print("Is Alphabets? ", lastname.isalpha())
print("Is Lowercase? ", lastname.islower())
print("Is Uppercase? ", lastname.isupper())
print("Is Printable? ", name.isprintable())
print("Is Space? ", name.isspace())

title = "Indian Standards Institute"
print("Is Title? ", title.istitle()) #first letter of first word capitalise
print("Swap Case: ", title.swapcase())

str = "hello, I am good"
print(str.title())

