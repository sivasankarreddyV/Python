#to print factorial of given number
def fact(n):
    s=1
    for x in range(1,n+1):
        s=s*x
    print("the factorial of n is:",s)
fact(5)

