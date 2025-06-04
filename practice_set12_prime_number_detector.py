a=int(input("enter a number: "))
prime=False
for i in range(2, a):
    if (a%i!=0):
        prime=True
if prime:
    print("this is a prime number")        
else:
    print("this is not a prime number")    