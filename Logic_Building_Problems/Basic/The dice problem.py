#The dice problem | Date:11-07-2026
num=int(input("Enter the dice number"))
if(num>6 or 1>num):
    print("Please enter valid dice number")
else:
    print(f"The opposite of the number {num} is {7-num}")