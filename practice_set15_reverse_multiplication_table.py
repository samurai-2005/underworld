n=int(input("enter a number for multiplication:  "))
m=int(input("enter an ending number:  "))
for i in range (m,0,-1):
    print(f"{n} X {i} =", n*i)
print("done")   