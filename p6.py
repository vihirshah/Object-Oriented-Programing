class Parent1():
    def set_str1(self,str1):
        self.str1=str1
    
    def show_str1(self): 
        return self.str1

class Parent2():
    def set_str2(self,str2):
        self.str2=str2

    def show_str2(self):
        return self.str2

class child(Parent1,Parent2):
    def set_str3(self,str3):
        self.str3=str3

    def show_str3(self):
        return self.str3




p1 = child()

fname=input("Enter your first name --> ")
mname=input("Enter your middle name --> ")
lname=input("Enter your last name --> ")
p1.set_str1(fname)
p1.set_str2(mname)
p1.set_str3(lname)

lst = [p1.show_str1(),p1.show_str2(),p1.show_str3()]

for i in lst:
    print(i,end=' ')

