# print("Learn Basics and Input taken by User in Python :-->")

# print("Hello Vishal Jaiswada!")
# print("He is a software Engineer,","Coder,","Problems Solver,","and a Teacher")

# name = "Vishal Jaiswada"
# age=23
# price=50.7

# print("My name is : ", name)
# print("My age is :",age,"years")
# print("My Salary is :",price,"LPA")

# print(type(name))
# print(type(age))
# print(type(price))

# # Sum of two numbers
# a=10
# b=5
# sum=a+b
# print("Sum of two numbers :",sum)

# # difference
# diff=a-b
# print("Difference of two numbers :",diff)

# # product
# product = a*b
# print("Product of two numbers :",product)

# #division
# division =a/b
# print("Division of two numbers :",division)

# # Exponentiation

# exponentiation = a**b
# print("Exponentiation of two numbers :",exponentiation)

# # Operators
# """
# Logical Operators :
# """
# print(not False) #true
# print(not True) #false

# val1=True
# val2=False
# print("AND operator:", val1 and val2)
# print("OR Operator:", val1 or val2)

# #Type conversion
# a=2
# b=5.75

# #implicit conversion
# print(a+b)

# #explicit conversion
# a1="2"
# b1=7.75
# print(float(a1)+b1)

# #another example
# a=7
# a=str(a)
# print(a)
# print(type(a))


# ## Take Input in Python
# name = input("Enter User Name :")
# print("User Name is:",name)
# print(type(name))

# #It will always give the string at output
# #so to convert it int --> int() ,for float --> float() etc

# age =int(input("Enter your age :"))
# print("Age is:",age)
# print(type(age))

# # sum of two numbers input by users
# num1 =int (input("Enter first number :"))
# num2 =int (input("Enter second number :"))

# sum=num1+num2
# print("Sum of Two numbers :",sum)

# #list
# list=[]

# n=int(input("Enter list of numbers :"))

# for i in range(n):
#     ele=int(input(""))
#     list.append(ele)

# print("List of numbers :",list)

# # Store different types of elements in list

# mixed_list=[1,"Hello",2.5,True]
# print("Mixed List :",mixed_list)

# marks={}
# n=int(input("Enter numbers of subjects :"))

# for i in range(n):
#     marks[i]=int(input(""))
    

# print(marks)

# marks ={}
# x=int(input("Enter physics marks :"))
# marks.update({"physics":x})

# y=int(input("Enter Chemistry marks :"))
# marks.update({"chemistry":y})

# z=int(input("Enter Math marks :"))
# marks.update({"math":z})

# print(marks)

# Loop Concept -->

# i=1
# while (i<=5):
#     print("Namaste Coder Bhaiyo!")
#     i+=1

## Print number 100->1
# num=100

# while num>=1 :
#     print(num)
#     num-=1


## Question-> multiplication table of a number n
# n = int(input("Enter the number of which multiplication :"))

# i=1
# while i<=10:
#     print(n,"X",i,"=",n*i)
#     i+=1

# Question--> square of 1-10
# i=1
# while i<=10:
#     print(i*i)
#     i+=1

# Question--> Fibonacci series upto n

# n=int(input("Enter the numbers:"))
# a=0
# b=1
# i=3
# print(a)
# print(b)
# while i<=n:
#     c=a+b
#     print(c)
#     a=b
#     b=c
#     i+=1


#Question--> Search for a number x in this tuple using loop

# list = [1,4,9,16,25,36,49,64,81,100]
# x = int(input("Enter the numbers:"))
# i=0 
# match =False
# while i<len(list):
#     if list[i]==x:
#         match=True
#         break
#     i+=1

# if match:
#     print("Number found at position:",i+1)
# else:
#     print("No number found at any position:")


# Question--> Factotial of a number using for loop
#by default range(n) ,range(1,n) or range(init,maxsize,stepsize)-->range(1,n,1)

x = int(input("Enter the numbers:"))
fact=1

for i in range(1,x+1):
    fact*=i

print("Factorial of",x,":",fact)






