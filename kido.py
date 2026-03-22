#this is a just learing process of oops with a program
class person:
    def __init__(self,n,a,s):
        self.name= n
        self._age= a
        self.__salary= s

    def show_private(self):
        print(f"the salary of {self.name} is {self.__salary}")

n=input("enter the name: ")
a=int(input("enter the age: "))
s=int(input("enter the salary: "))

p=person(n,a,s)
print("enter 1 for know about the details of the person")
choice=int(input("enter your choice: "))
if choice==1:
    print(p.name)
    print(p._age)
    
else:
    print("invalid choice")
print("if u need to know about the salary of the person then enter 1:")
choice=int(input("enter your choice: "))
if choice==1:
    password=int(input("enter the password: "))
    
    if password==1234:
        p.show_private()
    else:
        print("invalid password")