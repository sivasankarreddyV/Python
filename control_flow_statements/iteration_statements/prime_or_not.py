#to print prime or not using for loop
n=int(input("enter the number: "))
c=0
for i in range(1,n+1):
    z=n%i
    if z==0:
        c+=1
if c==2:
    print("it's prime")
else:
    print("it's not a prime")


