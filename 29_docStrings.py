# docstrings helps us to understand the function, class or module by appearing right after the the definition of the particular. They are not comments and are treated special by the interpreter of python.
# They are used to document  the code and tell the user about it.

def square(n):
    '''square(n) is a function that takes a number as an input and returns the square as output'''
    return n*n

print(square.__doc__)
number = int(input("Enter the value of num:"))
print(f"Square of {number} is: ", square(number))


# what is PEP8(Python Enhancement Proposal): guidelines for writing the best python programs. 
# Zen of Python: A short poem by Tim Peters which tells very beautifully defines and explains way, regret, while of after coding. You can read this at python interpreter: import this.