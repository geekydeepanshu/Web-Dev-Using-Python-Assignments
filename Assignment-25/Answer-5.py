class calculator:
    def __init__(self):
        self.num1=None
        self.num2=None
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1 + self.num2)
    def substract(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1 - self.num2)

c=calculator()
c.add(25,15)
c.substract(25,15)