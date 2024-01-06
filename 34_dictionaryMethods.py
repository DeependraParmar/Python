info = {
    'name': 'Deependra Parmar',
    'age': 20,
    'address': 'mp',
}

info.update({'age':21})
print("Dictionary after updating age is: ", info['age'])

# info.clear() # clear the whole dictionary and removes all the key value pairs from it

# info.pop(info['address']) removes the item with key address

# info.popitem() removes the last item from the dictionary

# del info['age'] deletes the item and if key is not found, it will delete the dictionary entirely

# del info : deletes the whole dictionary

