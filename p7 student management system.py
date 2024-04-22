class Student():
    def __init__(self,name,std,rnum,ano,age,gender) :
        self.name = name
        self.std = std
        self.rnum = rnum
        self.ano = ano 
        self.age = age
        self.gender = gender

    def display_info(self):
        print('''\tname --> {}
        roll number --> {}
        standard --> {}
        addmission no. --> {}
        age --> {}
        gender --> {} '''.format(self.name,self.rnum,self.std,self.ano,self.age,self.gender))
        

class StudentManagementSystem():

    def __init__(self):
        self.students = []

    def add_record(self,student):
        
        self.students.append(student)

    def display_list(self):
        for student in self.students:
            student.display_info()

    


# main 

n = int(input("enter number of record --> "))
student=[]
for i in range(n):
    name=input("enter your name --> ")
    std=int(input("enter your standar --> "))
    rnum=int(input("enter your roll number --> "))
    ano=int(input("enter your addmission number --> "))
    age=int(input("enter your age --> "))
    gender=input("enter your gender --> ")

    stu = Student(name,std,rnum,ano,age,gender)

    student.append(stu)

s1=StudentManagementSystem()
for i in student:
    s1.add_record(i)


s1.display_list()



