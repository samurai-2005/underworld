def perfect_square(a):
    b= a**0.5
    b=float(b)
    d=str(b)
    y=d[0:4]
    z=len(y)
    if d[2]!=0:
     return ("its not a perfect square")
    #if type(b) == float:
     #return ("its not a perfect square")
    elif z == 1:
       return (f"{ b} is perfect square root of {a}")


a=int(input("enter a number to check whether it is perfect square or not: \n "))

b=perfect_square(a)

print(b)