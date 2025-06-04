a=input("enter your name:- \n")
b=input("enter today\'s date:- \n")


letter ='''dear <|name|>,
                you are selected!
                <|date|>'''

letter = letter.replace("<|name|>",a)
letter = letter.replace("<|date|>",b)
print(letter)