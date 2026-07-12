#Sum of squares of n natural numbers | Date:11-02-2026

num=int(input("ENTER YOUR Nth NUMBER:"))
sum=0
for i in range(num+1):
    sum+=i**2
print("SUM OF SQUARES OF {} NATURAL NUMBERS IS {}".format(num,sum))