#to print the number is prime or not


def prime():
    c=0
    for i in range(1,num+1):
        z=num%i
        if z==0:
            c=c+1
    if c==2:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
num=int(input("enter a number :"))
prime()

