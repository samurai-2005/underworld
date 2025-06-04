name=input("please enter your name: \n")
marks1=int(input(f"hey {name}, please enter your math\'s marks: \n"))
marks2=int(input("please enter your science\'s marks: \n"))
marks3=int(input("please enter your computer\'s marks: \n"))

total= marks1 + marks2 + marks3

marks1_percentage = (marks1/100)*100
marks2_percentage = (marks2/100)*100
marks3_percentage = (marks3/100)*100
total_percentage = (total/300)*100

print(f"{name} your total number is {total} and your percentage is {total_percentage}%")

#if(total_percentage<40 and marks1_percentage<33):
#    print("you are FAIL in maths!!!")
#else:
#    print()    
#if(total_percentage<40 and marks2_percentage<33):
#    print("you are FAIL in science!!!")
#else:
#     print() 
#if(total_percentage<40 and marks3_percentage<33):
#    print("you are FAIL in computer!!!")
#else:
#    print() 
    
if(total_percentage<40):
    print("you are FAIL!!!")
elif(marks1_percentage<33):
    print("you are FAIL in math\'s")
elif(marks2_percentage<33):
    print("you are FAIL in science")        
elif(marks3_percentage<33):
    print("you are FAIL in computer") 
else:
    print("you are PASS")       