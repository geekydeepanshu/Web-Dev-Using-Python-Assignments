class Employee:
    def __init__(self):
        self.__empid=None
        self.__name=None
        self.__salary=None
    def set_empid(self,empid):
        self.__empid=empid
    def set_name(self,name):
        self.__name=name
    def set_salary(self,salary):
        self.__salary=salary
    def get_empid(self):
        return self.__empid
    def get_name(self):
        return self.__name
    def get_salary(self):
        return self.__salary



e=Employee()
e.set_empid(251341)
e.set_name("Deepanshu")
e.set_salary(100000)
print(e.get_empid())
print(e.get_name())
print(e.get_salary())