def removenth(a,b):
    a =str(a)
    b =int(b)
    
    y=""
    
    if len(a) >= b:
      z=a[b]
      c = a.replace(z,y)
      return c
    elif len(a)< b:
         return a
a =input("enter a string: ")
b =int(input("enter an integer: "))

c=removenth(a,b)
print(c)