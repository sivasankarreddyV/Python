#to print factors count for a given number
num=int(input("enter the number :"))
for i in range(1,num+1):
    if num%i==0:
        print(i)

