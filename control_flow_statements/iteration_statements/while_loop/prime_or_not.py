#to check prime or not
n=int(input("enter a number:"))
i=1
c=0
while i<n+1:
    z=n%i
    i+=1
    if z==0:
        c+=1
if c==2:
    print("prime:",n)
else:
    print("not prime:",n)

