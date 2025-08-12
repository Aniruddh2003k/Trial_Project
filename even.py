class Numbers:
    def __init__(self,n):
        self.n = n

    def even(self):
    
        if self.n % 2 == 0:
            return True
        else:
            return False

    def odd(self):
    
        if self.n % 2 != 0:
            return True
        else:
            return False

    def is_prime(self):
        count = 0
        if self.n <= 1:
            print(self.n," is not a prime number")
        for i in range(2,self.n):
            if self.n % i == 0:
                return False
        return True

a = int(input("Enter a number: "))
s = input("Enter any 1 option if you want to check your number to be 'even', 'odd' or 'prime': ")

n1 = Numbers(a)


if s == 'even':
    if n1.even():
        print("It is an even number")
    else:
        print("It is not an even number")

if s == 'odd':
    if n1.odd():
        print("It is an odd number")
    else:
        print("It is not an odd number")
    
if s == 'prime':
    if n1.is_prime():
        print("It is a prime number")
    else:
        print("It is not a prime number")

if s != 'even' and s != 'odd' and s != 'prime':
    print("Please enter a valid choice: 'even', 'odd', 'prime':  ")
