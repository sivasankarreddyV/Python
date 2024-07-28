#to filter  only even numbers from the list by using filter
#without lambda function
def iseven(x):
    if x%2==0:
        return True
    else:
        return False
l=[1,2,3,4,5,6,7,8,9,10]
l1=list(filter(iseven,l))
print(l1)
