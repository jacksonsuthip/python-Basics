# %%
# class variables shared across all the objects of the class
class Office:
    rent = 10000
    total = 0 
    
    def __init__(self,name):
        self.Name = name
        Office.total = Office.total + 1
    
    def member(self,paied):
        # instance(self)
        self.rent = self.rent - paied
        # class(Office)
#         Office.rent = Office.rent - paied
    

a = Office("anto")
b = Office("Jack")

paied1 = a.member(5000)

print("a -",a.rent)
print("b -",b.rent)


paied = a.member(5000)

print("total -",Office.total)


# %%
#class method & static method
class Home:
    addr = "nagercoil"
    def __init__(self,name,phno):
        self.Name = name
        self.PhNo = phno
        
    @classmethod
    def change_address(cls, address):
        cls.addr = address
        
    @staticmethod
    def pc(cName):
        available_pc = ["HP","Dell"]
        if cName in available_pc:
            return True
        return False
        
p1 = Home("anto",8877)
p2 = Home("jack",7788)

a = p1.change_address("ngl")

print(p1.addr)
print(p2.addr)
print(Home.addr)
print(p1.pc("HP"))

# %%



