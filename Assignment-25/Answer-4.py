class Profile:
    platform="iNeuron"
    def __init__(self):
        self.name=None
        self.__email=None
        self.__age=None
    def set_name(self,name):
        self.name=name
    def set_email(self,email):
        self.__email=email
    def set_age(self,age):
        self.__age=age
    def get_name(self):
        print(self.name)
    def get_email(self):
        print(self.__email)
    def get_age(self):
        print(self.__age)
    @classmethod
    def get_platform(cls):
        print(cls.platform)

p1=Profile()
p1.set_name("Deepanshu")
p1.set_email("saini1234deepanshu@gmail.com")
p1.set_age(20)
p1.get_name()
p1.get_email()
p1.get_age()
p1.get_platform()