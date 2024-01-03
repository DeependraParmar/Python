import time
hours = int(time.strftime("%H"))
minutes = int(time.strftime("%M"))
seconds = int(time.strftime("%S"))


if(hours>=0 and hours<=11):
    print("Good Morning Sir")

elif(hours>=12 and hours<=17):
    print("Good Afternoon Sir")
    
else:
    print("Good Evening Sir")