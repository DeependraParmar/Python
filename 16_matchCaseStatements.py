x = int(input("Enter the value of x: "))

match x:
    case 0:
        print("x is zero")
    
    case 1:
        print("x is one")
    
    case _:
        print("x is neither 0 nor 1")