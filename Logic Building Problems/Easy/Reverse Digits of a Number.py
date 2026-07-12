#Reverse Digits of a Number | Date:12-07-2026
num=int(input("Enter your number: ")) # To get the number from user
rev=0 # For Storing the Reversed number
while(num!=0):
    rem=num%10 
    rev=rev*10+rem
    num//=10
print("The reversed number is",rev)