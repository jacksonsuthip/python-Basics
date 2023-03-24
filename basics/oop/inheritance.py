# %%
class Home:
    addr = "nagercoil"
    
    def __init__(self,name,phno):
        self.Name = name
        self.PhNo = phno
        
    def pc(self,pcName):
        value = f"name : {self.Name} --- PC : {pcName}"
        return value

# inheritance
class Room(Home):
    addr = "Ngl"
    def __init__(self,name,phno,year):
        # dont repete (self.Nmae = name , ...) use super() mtthod
        super().__init__(name,phno)
        self.Year = year
    
p1 = Home("anto",8877)
p2 = Home("jack",7788)
print(p1.Name)
print(p2.pc("HP"))
print(p1.addr)

p3 = Room("suthip",5566,2010)
print(p3.addr)
print(p3.Year,p3.Name)



# %%



