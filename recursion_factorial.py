def factorial_recersive(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recersive(n-1)

a= factorial_recersive(10)
print(a)