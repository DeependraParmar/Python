# manipulate tuples: tuple >>> list, change list and then >>> tuple
# you can also merge two tuples using + Operator

tpl = (1,2,3,4,5,6)
lst = list(tpl)

lst.append(10)
lst.pop(2)
lst[2] = 20

tpl = tuple(lst)
print("Updated tuple is: ", tpl)


# count(): returns the count of an element in the tuple
# index(): returns the first occurence of the element provided and return the value error when not found
