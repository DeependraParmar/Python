# Strings are collection of characters, numbers, symbols, etc. A String is enclosed in single/double quotes ""/''. For eg. "My name is Deependra Parmar"

# single line string 
a = "Hello there, I am good. Thanks for asking!"
print(a)

print()

b = """Hello,
there I am good,
Thanks for asking!"""
print(b)
print()


# Indexing in Strings : If we try to access invalid index, we'll get Index Out of Range Error
name = "Deependra"
print("First character of name is: ", name[0])
# print("10th character of name is: ", name[10]) gives and error


# Using loop with strings
for i in name:
    print(i,sep=" ")