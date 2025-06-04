a=int(input("enter a number: \n"))

for n in range(2,a):
    if a%n==0:
        print("its not a prime number")
    else:
        print("its a prime number")