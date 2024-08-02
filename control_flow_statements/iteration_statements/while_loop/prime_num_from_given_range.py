#to print prime numbers within the given limit
start = 10
end = 50
print(f"Prime numbers between {start} and {end} are:")
n = start
while n <= end:
    if n > 1:
        divisor = 2
        is_prime = True   
        while divisor * divisor <= n:
            if n % divisor == 0:
                is_prime = False
                break
            divisor += 1
        if is_prime:
            print(n)
    n += 1

