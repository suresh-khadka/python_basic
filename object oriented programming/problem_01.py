class employee:
    name="suresh"
    faculty="nce"
    batch=2080

    def get_detail(self):
        print(f"my name is {self.name}. I am a {self.batch} batch.")


    @staticmethod
    def detail():
        print("enter your name")

a=employee()
print(a.name)
a.name="kapil"
print(a.name)
a.get_detail()
a.detail()