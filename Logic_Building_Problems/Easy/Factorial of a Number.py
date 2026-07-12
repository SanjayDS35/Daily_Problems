#Factorial of a Number | Date:12-07-2026

num=int(input("Enter your number: "))
fact=1
if num<0:
    print("Enter a valid number")
elif num==0:
    print(f"Factorial of the number {num} is 0")
else:
    for i in range(1,num+1):
        fact*=i
    print(f"Factorial of the number {num} is {fact}")
