class Number:
    def sum(self):
        return self.a + self.b

num = Number()
num.a = int(input("enter first number: "))
num.b = int(input("input second number: "))
s = num.sum()
print(s)
