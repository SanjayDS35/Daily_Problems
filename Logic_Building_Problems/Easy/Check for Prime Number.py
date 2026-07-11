#Check for Prime Number | Date:12-07-2026
num=int(input("Enter your number: ")) # To get the number from user
des= True # Declaring a variable for bool expressions
if num<=1: # The number cannot be less than or equal to 1
    des=False
for i in range(2,num):
    if(num%i==0):
        des= False
if(des==True):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")