class Profile:
    def __init__(self):
        self.name=None
        self.email=None
        self.age=None
    def set_name(self,name):
        self.name=name
    def set_email(self,email):
        self.email=email
    def set_age(self,age):
        self.age=age
    def get_name(self):
        print(self.name)
    def get_email(self):
        print(self.email)
    def get_age(self):
        print(self.age)

p1=Profile()
p1.set_name("Deepanshu")
p1.set_email("saini1234deepanshu@gmail.com")
p1.set_age(20)
p1.get_name()
p1.get_email()
p1.get_age()