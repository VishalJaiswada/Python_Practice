print("Learn Basics and Input taken by User in Python :-->")

print("Hello Vishal Jaiswada!")
print("He is a software Engineer,","Coder,","Problems Solver,","and a Teacher")

name = "Vishal Jaiswada"
age=23
price=50.7

print("My name is : ", name)
print("My age is :",age,"years")
print("My Salary is :",price,"LPA")

print(type(name))
print(type(age))
print(type(price))

# Sum of two numbers
a=10
b=5
sum=a+b
print("Sum of two numbers :",sum)

# difference
diff=a-b
print("Difference of two numbers :",diff)

# product
product = a*b
print("Product of two numbers :",product)

#division
division =a/b
print("Division of two numbers :",division)

# Exponentiation

exponentiation = a**b
print("Exponentiation of two numbers :",exponentiation)

# Operators
"""
Logical Operators :
"""
print(not False) #true
print(not True) #false

val1=True
val2=False
print("AND operator:", val1 and val2)
print("OR Operator:", val1 or val2)

#Type conversion
a=2
b=5.75

#implicit conversion
print(a+b)

#explicit conversion
a1="2"
b1=7.75
print(float(a1)+b1)

#another example
a=7
a=str(a)
print(a)
print(type(a))


## Take Input in Python
name = input("Enter User Name :")
print("User Name is:",name)
print(type(name))

#It will always give the string at output
#so to convert it int --> int() ,for float --> float() etc

age =int(input("Enter your age :"))
print("Age is:",age)
print(type(age))

# sum of two numbers input by users
num1 =int (input("Enter first number :"))
num2 =int (input("Enter second number :"))

sum=num1+num2
print("Sum of Two numbers :",sum)

#list
list=[]

n=int(input("Enter list of numbers :"))

for i in range(n):
    ele=int(input(""))
    list.append(ele)

print("List of numbers :",list)

# Store different types of elements in list

mixed_list=[1,"Hello",2.5,True]
print("Mixed List :",mixed_list)

marks={}
n=int(input("Enter numbers of subjects :"))

for i in range(n):
    marks[i]=int(input(""))
    

print(marks)

marks ={}
x=int(input("Enter physics marks :"))
marks.update({"physics":x})

y=int(input("Enter Chemistry marks :"))
marks.update({"chemistry":y})

z=int(input("Enter Math marks :"))
marks.update({"math":z})

print(marks)
