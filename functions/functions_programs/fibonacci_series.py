
#to print the fibonacci series using functions
def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
    print()
fibonacci(10)

