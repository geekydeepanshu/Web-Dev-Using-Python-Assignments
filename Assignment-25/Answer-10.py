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

class truecaller:
    def __init__(self):
        self.__data={}
    def add_data_base(self,number,name):
        self.__data[number]=name
    def fetch_name_base(self,number):
        try:
            name=self.__data[number]
            print(name)
        except KeyError:
            print("Given Number is Not present In True caller DataBase")
            if input("Do You want to add this data to DataBase[Y/N]:  ")=="Y":
                name=input("Enter Name for Given Number: ")
                self.add_data_base(number,name)
            else:
                pass
    def add_data(self):
        self.add_data_base(int(input("Enter a Phone Number:")), input("Enter Name: "))
        while True:
            if input("Do You want to add more Data[Y/N]:  ") == "Y":
                self.add_data_base(int(input("Enter a Phone Number:")), input("Enter Name: "))
            else:
                break
    def fetch_name(self):
        self.fetch_name_base(int(input("Enter Number To Be Acceseed: ")))
        while True:
            if input("Do You want to access more Data[Y/N]:  ") == "Y":
                self.fetch_name_base(int(input("Enter Number To Be Acceseed: ")))
            else:
                break



class smartphone(phone,calculator2):
    def fetch_name_inSmartPhone(self,t):
        t.add_data()
        t.fetch_name()


t = truecaller()
s=smartphone()
s.calling()
s.sms()
s.add(45,7)
s.substract(78,56)
s.divide(45,5)
s.fetch_name_inSmartPhone(t)
