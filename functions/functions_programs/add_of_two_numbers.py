#to print addition of two numbers using functions
#without argument without return type
def calc_add():
    m=int(input("enter first number: "))
    n=int(input("enter second number: "))
    add=m+n
    print(add)
calc_add()



#without argument with return type
def calc_add():
    m=int(input("enter first number: "))
    n=int(input("enter second number: "))
    add=m+n
    return add
add=calc_add()
print(f"area is :{add}")



#with argument without return type
def calc_add(m,n):
    m=int(input("enter first number: "))
    n=int(input("enter second number: "))
    add=m+n
    print(f"area is :{add}")
add=calc_add(4,5)



#with argument with return type
def calc_add(m,n):
    m=int(input("enter first number: "))
    n=int(input("enter second number: "))
    add=m+n
    return add
add=calc_add(4,5)
print(f"area is :{add}")


