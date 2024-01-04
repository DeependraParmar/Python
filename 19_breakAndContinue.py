n = int(input("Enter the value of n to print table: "))


for i in range(1,12):
    if(i == 10):
        break

    if(i%2 == 0):
        continue


    print(n ,"*",i , "=", n*i)

    