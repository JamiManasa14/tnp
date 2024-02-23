def isprime(n):
    if n==2:
        return "It's a prime & even number"
    for i in range(2,int(n**0.5)+1):
        print(f"{i} this much of time executed")
        if n % i == 0:
            return "it's not a prime number"
        
    return "it's a prime number"
         
print(isprime(17))