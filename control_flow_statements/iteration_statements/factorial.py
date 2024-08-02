#to print factorial of a given number
n=int(input("enter the number: "))
s=1
for i in range(1,n+1):
    s=s*i
print(f"the factorial of {n} is {s}")


