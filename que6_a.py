

     
    
with open('open.txt') as f:
    content=f.read()

if "1" in content:
     content= content.replace("1", "one")
if "2" in content:
     content= content.replace("2", "two")
if "3" in content:
     content= content.replace("3", "three")
if "4" in content:
     content= content.replace("4", "four")
if "5" in content:
     content= content.replace("5", "five")
if "6" in content:
     content= content.replace("6", "six")
if "7" in content:
     content= content.replace("7", "seven")
if "8" in content:
     content= content.replace("8", "eight")
if "9" in content:
     content= content.replace("9", "nine")
if "0" in content:
     content= content.replace("0", "zero")

f1=open('open.txt','w' )
f1.write(content)
f1.close











