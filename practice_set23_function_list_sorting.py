def line2( a=5 ):
    
    numbers = [7,3,13,6,8,5,1,2,4,15,9,10,12,14,11]
    list1=[]
    for item in numbers:
        if item<=a:
            list1.append(item)
    return list1

def line(num):
    num=int(num)
    numbers = [7,3,13,6,8,5,1,2,4,15,9,10,12,14,11]
    list1=[]
    for item in numbers:
        if item<=num:
            list1.append(item)
    return list1

a=input("enter a number: ")
c=line2()
b=line(a)
print(c)
print(b)

