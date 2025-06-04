l=[1,2,3,4,5,6,7,8,9]
rvs=l[::-1]
def even(l1):
    l2=[]
    for item in l1:
        if (item%2==0):
            l2.append(item)
    return l2
def divide(l):
    l3=[]
    for item in l:
        a=(item/2)
        a=float(a)
        l3.append(a)
    return l3
ldivide=divide(l)
leven=even(l)
reverse=(rvs[0:5]+l[5:9])

print((len(l)/2))
print(rvs[0:9])
print(l[2:8])
print(leven)
print(l[4:9])
print(reverse)
print(ldivide)
