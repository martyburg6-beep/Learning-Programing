class employee:
    campany ="ITC"
    def show(self):
        print(f"the name of the empolyee{self.name} and the salary is {self.salary}")
class programmer(employee):
    campany="ITC Inforth"
    def showlanguage(self): 
        print(f"the name is {self.name} and he is the good with{self.language}language")

a = employee()
b =programmer()
print(a.campany,b.campany)