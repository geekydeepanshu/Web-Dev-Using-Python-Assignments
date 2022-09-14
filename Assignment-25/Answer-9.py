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


user1=truecaller()
user1.add_data()
user1.fetch_name()



