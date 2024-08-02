#to print factorial of given number
n= int(input("enter a number: "))
factorial=1
i=1
while i<=n:
  factorial=factorial*i
  i=i+1
print(f"the factorial of{n}is: {factorial}")

