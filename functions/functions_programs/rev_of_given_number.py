
#to print the reverse of a given number
def reverse_number(number):
    reverse_number=0
    while number>0:
        last_digit=number%10
        reverse_number=(reverse_number * 10) + last_digit
        number=number//10
    print("the reverse of the given number is",reverse_number)
reverse_number(1221)


