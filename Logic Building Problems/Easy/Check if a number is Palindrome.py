#Check if a number is Palindrome | Date:12-07-2026

num=int(input("Enter your number: "))

rev=0
if num<0:
    num*=-1
n=num
while(num!=0):
    rev=(rev*10)+num%10
    num//=10
if rev==n:
    print(f"The number {n} is palindrome")
else:
    print(f"The number {n} is not palindrome")