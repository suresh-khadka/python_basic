class employee:    #this is patrent class !!
    name ="suresh"
    company="google"

    def __init__(self):
        print ("i am a employee")

    def showDetail(self):
        print(f"your name is {self.name} and you are a employee of {self.company}")


class manager(employee):   #this is a child class (inheritance occur)

    def __init__(self):
        print("i am a manager")

    def detail(self):
        print(f"your name is {self.name} and you are a employee of {self.company}")



e=manager()
a=employee()
e.showDetail()