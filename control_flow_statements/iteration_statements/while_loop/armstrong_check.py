#to check arm strong number or not
num=int(input("enter a number:"))
c=0
temp=num
while temp>0:
    res=temp % 10
    c=c+(res+res+res)
    temp=temp//10
if c==num:
    print(f"{num} is aremstrong")
else:
    print(f"{num} is not armstrong")


