def rec_sum(n):
    if n==0 or n==1:
        return 1
    return n + rec_sum(n-1)

a= rec_sum(5)
print(a)