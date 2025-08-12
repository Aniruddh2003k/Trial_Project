def evenodd(a):
    if a % 2 == 0:
        return True
    else:
        return False
n = int(input("Enter a number: "))    
if n == 0:
    print("The number entered is 0")
if n == 1:
    print("The number entered is 1")

else:
    if evenodd(n):
        print(n,"is an even number")
    else:
        print(n,"is an odd number")

    