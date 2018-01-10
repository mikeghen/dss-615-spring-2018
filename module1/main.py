# Lab 1: Body Mass Index

height_meters    = 2.1
weight_kilograms = 89.5
body_mass_index  = weight_kilograms / (height_meters * height_meters)
print(body_mass_index)

# Lab 2: Slope of a line

m = 0.5
b = 3
x = 2
y = m * x + b
print(y)

m = 1//2
b = 3
x = 2
y = m * x + b
print(y)

# Lab 3: Word Math

hello = "Hello"
world = "World"
phrase = hello + " # " + world + "!"
print(phrase)

print(phrase.upper())

print(phrase.split('#'))

# Lab 4: List Math
students = ["Reinaldo", "Kelly", "Thomas", "Kin"]
num_students = len(students)
print(num_students)

first_student = students[0]
print(first_student)

last_student = students[-1]
print(last_student)

first_three_students = students[0:]
print(first_three_students)

last_three_students = students[-3:]
print(last_three_students)

first_student_initial = students[0][0]
print(first_student_initial)


# Lab 5: Structures

coordinates = [ [1,0], [2,0.5], [3,1], [4,1.5] ]

first_point = coordinates[0]
first_point_x = coordinates[0][0]
first_point_y = coordinates[0][1]
print(first_point)

slope = (coordinates[3][1] - coordinates[0][1]) / (coordinates[3][0] - coordinates[0][0])
print(slope)

# Lab 6: Decisions

costs      = 150000
revenues   = 145000
net_profit = revenues - costs

if costs > revenues:
    print("Give up, you lost ${0:,.2f}.".format(net_profit))
elif costs < revenues:
    print("Keep at it, you earned ${0:,.2f}.".format(net_profit))
else:
    print("No taxable income!")

x = 6
if x == 5:
    print(x)

# Lab 7: Iteration

principal = 1000
annual_interest = 0.035
account_balance = principal

for year in range(2015, 2020):
    account_balance += (account_balance * annual_interest)
    print("{0}: End of Year Balance = ${1:,.2f}".format(year, account_balance))

# Lab 8: List Loops

students = ["Reinaldo", "Kelly", "Thomas", "Kin"]

for student in students:
    print(student)
