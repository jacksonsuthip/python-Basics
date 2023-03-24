# %%
# use uppercase in 1st letter
class Student:
    pass 

stu1 = Student()
stu2 = Student()

print(stu1)

# instance variable
stu1.name = "anto"
stu1.phno = 88700

stu2.name = "jack"
stu2.phno = 23844

print(stu1.name)
print(stu2.name)

# %%
# to avoid manual instance variable creation
from datetime import date
class Home:
    # constructor
    def __init__(self,name,phno,year):
        # self holdes current object
        # to change it to instance variable
        self.Name = name
        self.phNo = phno
        self.year = year
        
    def address(self):
        addr = f"name : {self.Name} --- PHNO : {self.phNo}"
        return addr
    
    def age(self,year2):
        # date today
        current_year = date.today().year
        age1 =  current_year - self.year
        age2 =  current_year - year2
        return age1,age2

h1 = Home("anto",777,1997)
h2 = Home("Jack",888,1999)

print(h1.Name)
print(h2.phNo)

print(h1.address())
print(h2.age(1997))

# %%



