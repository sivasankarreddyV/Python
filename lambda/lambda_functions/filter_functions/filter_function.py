#to print filter function using basic function
def even(n):
    if n%2==0:
        return "even"
    else:
        return "odd" 
for x in range(11):
    res=even(x)
    print(res,x)
#to print using lamda filter function
l1=[1,2,3,4,5]
x=list(filter(lambda x:True if x%2==0 else False,l1))
print(x)

