#to print factors of a given number
number= int(input("enter a number: "))
i = 1
while i <= number:
    if number % i == 0:
        print(i)
    i += 1

