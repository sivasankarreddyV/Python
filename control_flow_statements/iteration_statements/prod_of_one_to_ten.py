#to print product of 1 to n numbers using for loop
n=int(input("enter a number: "))
product=1
for i in range(1,n+1):
    product=product*i
print(f"the product of {n} numbers is: {product}")

