class employee:
    @property
    def name(self):
        return f'{self.fname,self.lname}'

    @name.setter
    def name(self,name):
        self.fname=name.split(" ")[0]
        self.lname=name.split(" ")[1]

e=employee()
e.name="Suresh khadka"
print(e.lname,e.fname)