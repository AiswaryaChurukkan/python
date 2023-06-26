def primenum(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i==0:
            return False
        return True
primes=[i for i in range(1,101)if primenum(i)]
print (sum(primes))
