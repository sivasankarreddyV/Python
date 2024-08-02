#to print sum of digits of a number
number=int(input("enter a number: "))
sum=0
while number > 0:
    remainder=number % 10
    sum=sum+remainder
    number = number // 10
print(f"the sum of digit is: {sum}")


