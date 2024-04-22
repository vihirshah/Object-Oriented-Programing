class Empolyee():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def show_details(self):
        print("name of the employee --> ", self.name)
        print("age of the employee --> ", self.age)
        print("gender of the employee --> ", self.gender)

# main 

n=int(input("enter umber of employees working --> "))
list1=[]
for i in range(n):
    name=input("enter name --> ")
    age=int(input("enter age --> "))
    gender=input("enter gender --> ")
    
    p1=Empolyee(name,age,gender)
    list1.append(p1)

for x in list1:
    x.show_details()