#Sum of Digits of a Number | Date:12-07-2026
num=int(input("Enter your number: "))
s=0
while(num!=0):
    s+=num%10
    num//=10
print("The sum of digits are",s)
