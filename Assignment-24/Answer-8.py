class laptop:
    def __init__(self,brand,cpu,ram,hdd):
        self.brand=brand
        self.cpu=cpu
        self.ram=ram
        self.hdd=hdd
    def showConfig(self):
        print("Brand: {}, CPU: {}, RAM: {}, HDD: {}".format(self.brand,self.cpu,self.ram,self.hdd))
    @classmethod
    def sorted_list_ram(cls,*t):
        list_laptop,list_brand = [],[]
        for e in t:
            temp_tuple=(e.ram,e.brand)
            list_laptop.append(temp_tuple)
        list_laptop.sort()
        for  e in list_laptop:
            list_brand.append(e[1])
        print(list_brand)

laptop1=laptop("Dell","i5 10th Gen",4,"1 TB")
laptop2=laptop("Asus","i5 10th Gen",8,"512 GB SSD")
laptop3=laptop("MacBook","M-2",16,"2 TB")

laptop1.sorted_list_ram(laptop1,laptop2,laptop3)
