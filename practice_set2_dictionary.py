mydict = {
    "mitti" : "soil",
    "hawa" : "air",
    "pani" : "water",
    "bijli" : "electricity",
}
     
        
print(mydict.keys())
a=input("enter you word u wanna find:- \n")
#print("the meaning of your word is ",mydict[a])
print("the meaning of your word is ",mydict.get(a))