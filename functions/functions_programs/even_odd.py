#to print th number is even or odd using functions
#without argument without return type
def even_odd():
    n=int(input("enter second number: "))
    if n%2==0:
        print("even")
    else:
        print("odd")
even_odd()




#without argument with return type
def even_odd():
    n=int(input("enter the number: "))
    if n%2==0:
        return f" {n} is even"
    else:
        return f" {n} is odd"
result = even_odd()
print(result)




#with argument without return type
def even_odd(even_odd):
    n=int(input("enter the number: "))
    if n%2==0:
        print("even")
    else:
        print("odd")
even_odd(6)




#with argument with return type
def even_odd(even_odd):
    n=int(input("enter the number: "))
    if n%2==0:
        return f" {n} is even"
    else:
        return f" {n} is odd"
result = even_odd(6)
print(result)

