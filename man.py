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

#this is a program of encapuslation in oops's concept
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks    # private

    def get_marks(self):
        print(f"{self.name}has marks:{self.__marks}")
        
        # return marks properly

    def update_marks(self, new_marks):
        if 0 <= new_marks <=100:
            self.__marks=new_marks
            print(f"the upadated marks is {self.__marks}")
        else:
            print("the marks is should be between 0 to 100")
        # only update if marks between 0 and 100

s1 = Student("Aditya", 85)
s1.get_marks()
s1.update_marks(95)
s1.get_marks()
s1.update_marks(150)  # should show error message
#this is a program of inheritance in oops's concept
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}")


class Dog(Animal):
    def __init__(self,name,sound,owner):
        super().__init__(name,sound)
        self.owner=owner
    def fetch(self):
        print(f"{self.name} is a name and it make sound{self.sound} and its owner is {self.owner}")
    # add owner attribute
    # add fetch method

class Cat(Animal):
    def __init__(self, name, sound,indoor):
        super().__init__(name, sound)
        self.indoor=indoor
    def purr(self):
        print(f"{self.name} is a name and it make sound{self.sound} and its indoor is {self.indoor}")
    # add indoor attribute
    # add purr method


d1 = Dog("Bruno", "Woof", "Aditya")
d1.speak()
d1.fetch()

c1 = Cat("Whiskers", "Meow", True)
c1.speak()
c1.purr()

#this is a program of polymorphism in oops's concept
class Payment:
    def pay(self, amount):
        print("Processing payment...")

class CreditCard(Payment):
    def pay(self,amount):
            print(f"Paid ₹{amount} via Credit Card")
    # override pay method
    # print "Paid ₹{amount} via Credit Card"

class UPI(Payment):
    def pay(self,amount):
            print(f"Paid ₹{amount} via UPI")
    # override pay method
    # print "Paid ₹{amount} via UPI"

class NetBanking(Payment):
    def pay(self,amount):
            print(f"Paid ₹{amount} via Net Banking")
    # override pay method
    # print "Paid ₹{amount} via Net Banking"


payments = [CreditCard(), UPI(), NetBanking()]
for payment in payments:
    payment.pay(1000)

#This is a program of abstraction in oops's concept
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car is starting")
    def stop(self):
        print("car is stopping")
    # implement start
    # implement stop

class Bike(Vehicle):
    def start(self):
        print("Bike is starting")
    def stop(self):
        print("Bike is stopping")
    # implement start
    # implement stop


c = Car()
c.start()
c.stop()

b = Bike()
b.start()
b.stop()