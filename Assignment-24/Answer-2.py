import time
class user:
    def __init__(self):
        self.name=None
        self.age=None
        self.email=None
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



