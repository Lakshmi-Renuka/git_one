name = input("What is your name?")
color = input("What is your favorite color?")
print(name + ' likes ' + color)

birth_year = input("Enter your birth year: ")
print(type(birth_year))
age = 2026 - int(birth_year)
print(type(age))
print(age)

wlbs = input(" Weight (lbs)")
wkg = int(wlbs) * 0.45
print(wkg)

name = 'jennifier'
print (name[1:-1])

x = (2+3)*10-3 
print(x) # ans 47

is_hot = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")

is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

p = int(input("Enter principal amount: "))
credit = True
if credit:
    down_payment = 0.1 * p
else:
    down_payment = 0.2 * p
print(f"Down payment: ${down_payment}")

n= input("Enter your name: ")
if len(n) < 3:
    print("Name must be at least 3 characters") 
elif len(n) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")

w=int(input("Enter weight: "))
unit=input("Enter unit (K) for kilograms or (L) for pounds: ")
if unit.upper() == "K":
    print(f"Weight in pounds: {w * 2.20462}")
elif unit.upper() == "L":
    print(f"Weight in kilograms: {w * 0.453592}")
else:
    print("Invalid unit. Please enter 'K' for kilograms or 'L' for pounds.")


i=1
while i<=5:
    print('*' * i)
    i=i+1
print("Done")

sn=9
count = 0
limit=3
while count < limit:
    guess = int(input("Guess the number: "))
    count= count + 1
    if guess == sn:
        print("You won!")
        break
else:
    print("Sorry, you failed!")

import calendar
x=int(input("enter the year:"))
print("***********calender***********")
print(calendar.calendar(x))

# Addition of Matrices.
x=[[12,7,3],[4,5,6],[7,8,9]]
y=[[5,8,1],[6,7,3],[4,5,9]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (len(x)):
    for j in range (len(x[0])):
        result [i][j] = x[i][j]+y[i][j]
for r in result:
    print(r)

# Fibonacci Series.
n=int(input("enter the range:"))
f1=0
f2=1
for i in range(0, n+1):
     f3=f1+f2
     print (f3)
     f1=f2
     f2=f3
print("end of series")

# Random Number Generated between 1 and 100 and Even and Odd.
import random
x=random.randint(1,100)
print(x)
if(x % 2==0):
    print("even")
else:
    print("odd")

# Simple and Compound Interest.
p=float(input("enter principle amount:"))
t=float(input("enter time taken:"))
r=float(input("enter rate of interest:"))
si=(p*t*r)/100
print("simple interest:",si)
ci=p*((1+r/100)**t)-p
print("compound interest:",ci)
