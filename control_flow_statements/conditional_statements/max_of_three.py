#maximum of three numbers
a=int(input("enter a first number: "))
b=int(input("enter a second number: "))
c=int(input("enter a third number: "))
if a>b and a>c:
    print("a is max: ", a)
elif b>c:
    print("b is max: ", b)
else:
    print("c is max: ", c)
