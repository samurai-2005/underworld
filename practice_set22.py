def letter(l, date):
    for item in l:
        print(f'''dear {item},
                you are selected!
                 {date}''')
    
a = "22/10/2024"

l1=["aarav", "sohan", "brijesh", "anmol"]

letter(l1,a)
