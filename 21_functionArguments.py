def average(numsArray=[0], len=0): #numsArray with default argument as [0]
    sum = 0
    for i in numsArray:
        sum += i
    
    return sum/len

arr = [10,20,30,40]

print("Average of all numbers in the list is: ", average(len=len(arr),numsArray=arr)) # keyword arguments as if you want that the order of the arguments that are passed to not matter

# When there are no default arguments, all the arguments are called REQUIRED ARGUMENTS and there is no optional choice while passing the arguments.



# Taking an arguments as in iterable 

# 1. As TUPLE ------->
# def average(*numbers): here, numbers is tuple and you can iterate it.

# 2. DICTIONARY --------> 
# def printHello(**names): here, names is dictionary and you can use it as names["key"]


# At last, there is return statement which helps us to calculate something in the function and return a value