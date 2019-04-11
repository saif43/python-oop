def isPrime(n):
    if n < 2:
        return
    for i in range(2,n-1):
        if n%i==0:
            return
    print(n)
    
for i in range(int(input('Enter range: '))):
    isPrime(i)