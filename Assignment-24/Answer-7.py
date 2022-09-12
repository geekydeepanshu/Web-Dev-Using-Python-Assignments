class laptop:
    def __init__(self):
        self.brand=None
        self.cpu=None
        self.ram=None
        self.hdd=None
    def showConfig(self):
        print("Brand: {}, CPU: {}, RAM: {}, HDD: {}".format(self.brand,self.cpu,self.ram,self.hdd))



