class phone:
    def calling(self):
        print("Calling....")
    def sms(self):
        print("SMS...")
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

class smartphone(phone,calculator2):
    pass



s=smartphone()
s.calling()
s.sms()
s.add(45,7)
s.substract(78,56)
s.divide(45,5)