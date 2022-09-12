import time
class user:
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

user1=user()
user1.name="Deepanshu"
user1.age=19
user1.email="saini1234deepanshu@gmail.com"
user2=user()
user2.name="Shivam"
user2.age=21
user2.email="shivam1234mittal@yahoo.com"
