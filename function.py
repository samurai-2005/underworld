def max(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1
    else:
        if(num2>num3):
            return num2
        else:
            return num3
        
m= max(12,32,44) 
print(m)       


