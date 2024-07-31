#to print even or odd
num=int(input("enter a number: "))
def even_odd(num):
        if num%2==0:
            return "even"
        else:
            return "odd"
result=even_odd(num)
print(result)
