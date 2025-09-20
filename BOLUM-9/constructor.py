#class

class product:
    #attribute,properties
    def __init__(self,name,price,isActive):
        self.name=name
        self.price=price
        self.isActive=isActive

p1 = product("Laptop", 15000, True)
p2 = product("Klavye", 350, False)

urunler=[p1,p2]

for i in urunler:
    print(i.name+":"+str(i.price))