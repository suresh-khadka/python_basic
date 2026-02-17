class employee:
    name="suresh"
    faculty="nce"
    batch=2080

    def __init__(self,a,b,c):   #this is a dunder method.
        print("my name is suresh khadka.")
        self.name=a
        self.faculty=b
        self.batich=c

a=employee("roshan ","computer engineering",2081)
print(a.name,a.faculty)