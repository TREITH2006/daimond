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