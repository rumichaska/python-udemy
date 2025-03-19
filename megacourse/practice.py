# lists

student_grades = [9.1, 8.8, 7.5]
list_2 = [9, "hello", [1, 2, 4.33]]
list_range = list(range(0, 11))

print(student_grades)
print(list_2 + student_grades)
print(list_2 * 2)
print(list_range)


# dir()

dir(int)
dir(str)
dir(list)

# Methods

help(list.__iadd__)
help(str.upper)


# Mean of a list

mysum = sum(student_grades)
lenght = len(student_grades)
mean = mysum / lenght
print(mean)


# Dictionary (key: value)

student_grades_dict = {"juam": 15.0, "jose": 13.4, "maria": 12.0}
mysum = sum(student_grades_dict.values())
lenght = len(student_grades_dict.values())
mean = mysum / lenght
print(student_grades_dict.keys())
print(mean)


# Tuples (not mutable)

monday_temperatures = (1, 4, 5)
print(monday_temperatures)

student_grades.append(12.3)
monday_temperatures.count(1)
print(student_grades)


# Operations with lists

tuesday_temperatures = [9.2, 3.2, 1.2, 12]
tuesday_temperatures.append(2.12)
print(tuesday_temperatures)


# User input

def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"


user_input = float(input("Enter temperature:"))
print(weather_condition(user_input))


user_input = input("Enter your name: ")
message = f"Hello {user_input}!!"
print(message)


# String format

name = input("Enter your name: ")
surname = input("Enter your surname: ")
when = "today"
# Formas de darle formato
# message = "Hello %s %s" % (name, surname) # 1
# message = f"Hello {name} {surname}. What's up {when}" # 2
message = "Hello {} {}. What's up {}".format(name, surname, when) # 3
print(message)


# For loops

monday_temperatures = [9.1, 8.2, 2.3]
print(round(monday_temperatures[0]))
for temp in monday_temperatures:
    print(round(temp))

for letter in "hello":
    print(letter.title())


student_grades = {"Mary": 9.1, "Jose": 1.2, "Pingo": 2.1}
for grades in student_grades.items():
    print(grades)
for grades in student_grades.keys():
    print(grades)
for grades in student_grades.values():
    print(grades)


# While loops

a = 5
while a > 0:
    a-=1
    print(1)


usename = ""
while usename != "pypy":
    usename = input("Enter usename: ")


while True:
    username = input("Enter username: ")
    if username == "pypy":
        break
    else:
        continue
