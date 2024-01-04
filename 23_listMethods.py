colors = ["gray","green","red","blue","white","black","cyan"]
numbers = [10,9,8,7,6,5,4,3,2,1]

# append(): appends an item at the end of the list
colors.append("khaki")
print("Appended Khaki in colors: ", colors)
print()

# sort(): sorted the list
colors.sort()
numbers.sort(reverse=True) #sorting the numbers in the reverse order

print("Sorted colors is: ", colors)
print("Sorted numbers is: ", numbers)


# reverse(): reverses the list
# index(item): returns the first occurence index of the item in the list
# count(item): returns the count of the item in the list
# copy(list): returns the copy of the whole list which can be stored in another list
# insert(index,value): inserts the value at the index
# list1.extend(list2): extends the list1 with list2 as the list2 elements/items are added to the list1
# concatenation: list1 = list2 + list3