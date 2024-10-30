# OOPs Concept Lec-8 in python Series :

# Basic Class & Object Example:

# class Student:
#     name="vishal"
    
# s1=Student()
# print(s1.name)

# s2=Student()
# print(s2.name)

# class Car:
#     color="black"
#     brand="Tata Nexon"

#     def Speed(self):
#         return "Speed min.=40km & max.=60km"
#     def Engine(self):
#         return "Engine min. size=1.2 & max. size=1.5"

# car1= Car()
# print(car1.brand)
# print(car1.Speed())
# print(car1.Engine())


# Constructor in python code

# class Student:
    
#     #default constructor
#     # def __init__(self):
#     #     pass
        
#     #parameterized constructor
#     def __init__(self,fullname,rollno,marks):
#         self.fullname=fullname
#         self.rollno=rollno
#         self.marks=marks
#         print("Adding new student in Database...")
    
#     def welcome(self):
#         print("Welcome student,",self.fullname)
    
#     def get_marks(self):
#         return self.marks
    
# s1=Student("Vishal Jaiswada","001",95)
# print(s1.fullname,",Roll No.:",s1.rollno,",Marks:",s1.get_marks())

# s2=Student("Vikas Patel","002",97)
# print(s2.fullname,",Roll No.:",s2.rollno,",Marks:",s2.get_marks())

# Practice Question

# class Student:
#     def __init__(self,name,marks1,marks2,marks3):
#         self.name=name
#         self.marks1=marks1
#         self.marks2=marks2
#         self.marks3=marks3
    
#     def calculate_average(self):
#         return (self.marks1+self.marks2+self.marks3)/3
    
#     def get_highest_marks(self):
#         return max(self.marks1,self.marks2,self.marks3)

# s1=Student("Vishal Jaiswada",95,87,92)

# print("Name:",s1.name)

# print("Average Marks:",s1.calculate_average())

# print("Highest Marks:",s1.get_highest_marks())

# Static Methods :
# Methods that don't use the self parameter (work at class level)
# use @staticmethod in class

# class Student:
#     @staticmethod  #decorator
#     def college():
#         print("G L Bajaj ITM , Greater Noida")

# s1=Student()
# s1.college()

# OOPs Pillar => 4 types (Abstraction , Encapsulation , Inheritance , Polymorphism)

#1 Abstraction: Hiding Unnecessary details about class data and methods

# class Car:
#     def __init__(self):
#         self.clutch = False
#         self.accelerator = False
#         self.brk = False
    
#     def start(self):
#         self.clutch = True
#         self.accelerator = True
#         print("Car Started...")

# car1=Car()
# car1.start()

#2 Encapsulation: Hiding data and methods inside a class, making it secure and private
#Wrapping data and function into a single unit(object).

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    
    def debit(self,amount):
        if amount>self.balance:
            print("Insufficient Balance")
        else:
            self.balance-=amount
            print("Rs.",amount,"was Debited Successful")
            print("Total balance = ",self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was Credited Successful")
        print("Total balance = ",self.get_balance())
    def get_balance(self):
        return self.balance

acc1=Account(10000,123456)

acc1.credit(5000)

acc1.debit(4000)

acc1.credit(50000)

acc1.debit(15000)