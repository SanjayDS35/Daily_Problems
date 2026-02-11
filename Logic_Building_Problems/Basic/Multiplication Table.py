#Multiplication Table |  Date:10-02-2026

def printTable(num):
    for i in range(1,11):
        print("{} * {} = {} ".format(num,i,num*i))
num=int(input("ENTER YOUR NUMBER FOR TABLE:"))
printTable(num)