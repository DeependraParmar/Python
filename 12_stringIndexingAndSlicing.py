string = "Deependra Parmar"

print("Length of the string is: ", len(string))
print("First Name is: ", string[0:9]) # outer bound is not inclusive
print("String till 6: ", string[:7])
print("From 5 to end: ", string[5:])
print("Character at 10th index: ", string[10])
print("Negative Slicing: ", string[0:-4]) # interpreted as string[0: len(string)-4]
print("Negative Slicing again: ", string[-1:-8]) # interpreted as string(len(string)-1:len(string)-8) that is 15:8 ----> Nothing 😅😅


# looping through a string
alphabets = "abcdefghijklmnopqrstuvwxyz"
for i in alphabets:
    print(i)