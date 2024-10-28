# OOPs Concept Lec-8 in python Series :

# Basic Class & Object Example:

# class Student:
#     name="vishal"
    
# s1=Student()
# print(s1.name)

# s2=Student()
# print(s2.name)

class Car:
    color="black"
    brand="Tata Nexon"

    def Speed(self):
        return "Speed min.=40km & max.=60km"
    def Engine(self):
        return "Engine min. size=1.2 & max. size=1.5"

car1= Car()
print(car1.brand)
print(car1.Speed())
print(car1.Engine())