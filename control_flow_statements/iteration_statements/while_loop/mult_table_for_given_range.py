#to print multiplication tables within the given limit
n=int(input("enter a number:"))
i=1
while i<=n:
    j=1
    while j<=10:
        c=i*j
        print(f"{i} * {j} = {c}")
        j+=1
    i+=1


