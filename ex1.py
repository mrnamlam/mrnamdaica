# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("Hello, World.")
print(50+50)
print("50+50")
a=2468
b=1234
print("2468 + 1234 = ", a+b)
print("2468 - 1234 = ", a-b)
print("2468 * 1234 = ", a*b)
print("2468 / 1234 = ", a/b)
print("Perimeter =", (5+2)*2)

num_integer = 12
num_float = 12.345
string_var = 'I am gay.'
boolean_var = 'true'

print(num_integer)
print(num_float)
print(string_var)
print(boolean_var)
statement = "I love you, Sullivanilla."

print("hello, nice to meet you, " + statement)


date_of_birth = 23
print("Ngày sinh nhật của cục cưng: " + str(date_of_birth))

length = 7.8
width = 3.5

print("Area = ", str(length*width))
print("Perimeter= ", str((length+width)*2))

name_1 = input("Please enter your name: ") 
print("Hello, Mr. " + name_1)


name_2 = input("Please enter your name and age: ") 
age = int(input())

print("In 15 years ahead, age of Mr. " + name_2 + " will be " + str(age+15))

print("Find modulus, please enter number a:")
a = int(input())
print("Enter number b:")
b = int(input())

print("a % b =", a%b)
print("a % b = " + str(a%b))

c = int(input("Enter number c for swapping: "))
d = int(input("Enter number d for swapping: "))

e = c
c = d
d = e

print("After swap c = " + str(c) + " and d = " + str(d))

print("Enter a float radius r:")
r = float(input())

print("Area of a circle = " + str(3.14*r*r))
print("Circumference = " + str(2*3.14*r))

f = int(input("Compare between f and g, please enter integer f: "))
print("Please enter integer g:")
g = int(input())

print("f < g:", f < g)
print("f > g", f > g)

