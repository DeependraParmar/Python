# try except is used for error handling or exception handling in python 
# Whenever exception arises, the code after the line error occured stops. In order to make the program work seemlessly, we handle the exception in such a way that it does not breaks the flow of the program
# Prevents program to hault. In a nutshell, do something els when error occurs

try:
    n = int(input("Enter the value of n: "))
except ValueError as v:
    print("Value given is not integer")

try:
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
except:
    print("Unable to print table")

print("Very important code here")
print("Finally, this is the end of the program")