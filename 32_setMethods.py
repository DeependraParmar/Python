s1 = {1,3,5,7,6,9}
s2 = {2,4,6,8,3,7}

union = s1.union(s2)
# s1.update(s2)  # update the set s1 with the items of s2 not present in s1
print("Union of s1 & s2 is: ",union)

intersection = s1.intersection(s2)
# s1.intersection_update(s2) # updates the s1 with intersection of s1 & s2 and rest are removed from s1
print("Intersection of s1 & s2 is: ", intersection)

# symmetric difference: (s1 U s2) - (s1 intersection s2): non-common values
symmetric_difference = s1.symmetric_difference(s2)
# s1.symmetric_difference_update(s2) # updates s1 with non-common elements i.e. union-intersection
print("Symmetric difference of s1 and s2 is: ", symmetric_difference)

difference = s1.difference(s2)
print("Difference b/w s1 and s2 is: ", difference)

isDisjoint = s1.isdisjoint(s2)
print("Is s1 and s2 disjoint: ", isDisjoint)

isSubset = s1.issubset(s2)
print("Is s2 subset of s1: ", isSubset)

isSuperset = s1.issuperset(s2)
print("Is s1 superset: ", isSuperset)

s1.add(100)
print("s1 updated: ", s1)

# s1.remove(10) raises an error as the element 10  is not present in the set
s1.discard(99)
print("Elements removed from s1: ", s1)

item = s1.pop()
print("Last element popped from s1 but, we don't know what is popped😅😅: ", s1, end="\n")
print("Item popped is: ", item)

# using if else to check whether an element is present in the set or not 
if 2 in s2:
    print("2 is present in s2")
else:
    print("2 is not present")

s2.clear() # cleares whole items from the set
print(s2)

del s2 # deletes the whole set s2