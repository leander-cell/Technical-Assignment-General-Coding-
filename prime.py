n = int(input("Enter your number:"))

if n<=1:
    print(n, "is not a prime number")

else:
    for i in range(2, n +1 ):
       if n % i == 0:
           break
    if n == i:
        print(n, "is a prime number")
    
    else:
        print(n, "is not a prime number")
