class calculator:
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1 + self.num2)
    def substract(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1 - self.num2)
class calculator2(calculator):
    def multiply(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print(self.num1 * self.num2)
    def divide(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1/ self.num2)

c=calculator2()
c.add(25,15)
c.substract(25,15)
c.multiply(25,5)
c.divide(36,12)
