class employee:
    name="suresh"
    company_name="samsung"

    def showDetail(self):
        print(f"I am {self.name} and i am a employee of {self.company_name}")

class manager(employee):
    position="manager"

class customer(manager):

    def intro(self):
        print(f"your name is {self.name} and you are a employee of {self.company_name} at position {self.position}")

c=customer()
c.showDetail()
c.intro()