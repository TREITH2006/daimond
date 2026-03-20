class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"my name is {self.name},age id {self.age}")
        
        
s1=student("adithya", 19)
s1.introduce()

s2=student("sai", 20)

s2.introduce()
#this is a first day of class

#this is a second program of the learning
class bankaccount:
    def __init__(self,owner,balance):
        self.name=owner
        self.balance=balance
    def show(self):
        print(f"the owner of the account is {self.name} and the balance is {self.balance}")

b1=bankaccount("adithya", 1000)
b1.show()
b2=bankaccount("sai", 2000)
b2.show()

#the 3rd code 
class Zoo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def animal(self):
        print(f"The name of the animal is {self.name} and the age is {self.age}")

    def bird(self):
        print(f"The name of the bird is {self.name} and the age is {self.age}")


print("Welcome to the zoo")
print("1. Animals\n2. Birds")

choice = int(input("Enter your choice: "))

if choice == 1:
    name = input("Enter animal name: ")
    age = int(input("Enter animal age: "))
    obj = Zoo(name, age)
    obj.animal()

elif choice == 2:
    name = input("Enter bird name: ")
    age = int(input("Enter bird age: "))
    obj = Zoo(name, age)
    obj.bird()

else:
    print("Invalid choice")