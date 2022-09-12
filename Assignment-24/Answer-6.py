import time
class user:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
    def greet(self):
        struct_time=time.localtime()
        hour=int(time.strftime("%H",struct_time))
        if hour >= 0 and hour < 12:
            print("Good Morning, ",self.name)
        elif hour >= 12 and hour < 17:
            print("Good Afternoon, ",self.name)
        elif hour >= 17 and hour < 20:
            print("Good Evening, ",self.name)
        else:
            print("Good Night, ", self.name)
    @classmethod
    def youngest(cls,*t):
        list_age = []
        for e in t:
            list_age.append(e.age)
        list_age.sort()
        print("Youngest Users: ")
        for e in t:
           if e.age==list_age[0]:
               print(e.name)


user1=user("Deepanshu",19,"saini1234deepanshu@gmail.com")
user2=user("Shivam",22,"shivammittal1234@gmail.com")
user3=user("Aditi",20,"aditityagi@gmail.com")
user.youngest(user1,user2,user3)
