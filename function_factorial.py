def factorial(n):
    product=1
    for i in range(n):
         product=product*(i+1)
    return product 

f= factorial(5)
g=factorial(9)
print(f)   
print(g)