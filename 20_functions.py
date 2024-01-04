# Functions are re-usable block of code which helps us to implement DRY Principle.
# Here, we are having a list of three person in the list. We took the  principal, rate and time for each person and calculated simple interest for them. After that, we have returned the interests in the dictionary

def calculateSI(p,r,t):
    return (p*r*t)/100

def calculateCI(p,r,t):
    pass #pass keyword helps us to define a prototype of a function which you might want to define later on in the future


names = ["Deependra","Ravi","Sohan"]
interests = {}

for i in names:
    principal = float(input(f"Enter the principal amount for {i}: "))
    rate = float(input(f"Enter the rate for {i}: "))
    time = float(input(f"Enter the time for {i}: "))
    print()

    interests[i] = calculateSI(principal,rate,time)


print()
print("Corresponding Interest are: ", interests)
