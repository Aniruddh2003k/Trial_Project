def is_prime(n):
    count = 0
    if n <= 1:
        print(n," is not a prime number")
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = a+b
if is_prime(c):
    print(c," is a prime number")
else:
    print(c," is a prime number")
