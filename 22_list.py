# List is like an array which can store multiple datatypes in it as it is heterogeneous in nature. Item can also be a dictionary, string, int, boolean, etc.
# Its is an ordered collection of items and used to store multiple values or data in one variable
# Multiple items are seperated with comma and are enclosed in []
# Items can be accessed with index starting from 0 to len(list)-1
# Lists are mutable datatypes in Python

lists = [10,20,30,"Deependra","Rahul","Priya"]

for i in lists:
    print(i, end=" ")

# type of lists
print()
print("Type of lists: ", type(lists))
print()

# mutability of lists
print("Item at index 2 is: ", lists[2])
lists[2] = "ShubhamSaxena"
print("After changing, index 2 has: ", lists[2])

# slicing in lists
print()
print("Slicing lists from 2 to 4: ", lists[2:4]) # there is also a 3rd parameter of slicing i.e. step
print("Slcing List from -3 to -1: ", lists[-3:-1]) # interpreted as lists[len(lists)-3: len(lists)-1] 

# check whether Deependra is there in the list or not and same thing applies for strings as well
print()
if "Deependra" in lists:
    print("Yes, Deependra is there in list")
else:
    print("No, Deependra is not there in the list")
print()


# List comprehension in python i.e. creating a list at runtime
lcomp = []
sqlst = []
lcomp = [i for i in range(1,21,3)]
sqlst = [i*i for i in range(1,20) if i%2==0]
print("List generated using Comprehension is: ",lcomp)
print("Square list generated using Comprehension is: ", sqlst)