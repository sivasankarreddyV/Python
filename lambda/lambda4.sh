#using map function without lambda
l=[1,2,3,4,5,6,7,8,9,10]
def double(x):
    return 2*x
l1=list(map(double,l))
print(l1)
