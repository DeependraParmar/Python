# Dictionary is key value pair datatype which provides random access with the help of key index
# They are ordered in nature

dict = {
    "name": "Deependra Parmar",
    "age": 20,
    "class": "human",
    "gender" : "male"
}

print("Whole dictionary is: ",dict)
print("Name is: ", dict["name"])
print("Name is: ", dict.get("name2")) # name2 is not there so, do not throws an error


# getting the keys of the dictionary 
print("All keys of dictionary are: ", dict.keys())
print("All the values of the dictionary are: ", dict.values())
print("All the items are: ", dict.items())