# for loops helps us to iterate multiple time or I must say n times, you want.
# We can iterate iterable objects like strings, lists, dictionaries, etc.

# Iterating over a number n
n = int(input("Enter the value of n: "))

for i in range(1,n+1,2):
    print(i, end=" ")
print()
print()

# Iterating over a string
name = "Deependra Parmar"
for i in name:
    print(i, end=" ")
print()
print()

# Iterating over a list 
fruits = ["Apple","Banana","Chiku","Pomegranate","Strawberry"]
for i in fruits:
    for alpha in i:
        print(alpha,end=' ')