class person:
    def __init__(self,f_name,l_name,age,gender):
        self.f_name=f_name
        self.l_name=l_name
        self.age=age
        self.gender=gender

    def movement(self):
        print("Person is walking")

a = person("John","Doe",27,"Male")
print(a.f_name,a.l_name,a.age,a.gender)

b = person("Mary","Jane",34,"Female")
print(b.f_name,b.l_name,b.age,b.gender)

c = person("Jane","Doe",21,"Female")
print(c.f_name,c.l_name,c.age,c.gender)