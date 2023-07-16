# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")


#----------------

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

#----------------

# students = []
    
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")

# for student in sorted(students):
#     print(student)

#----------

# students = []
    
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         students.append(student)

# for student in students:
#     print(f"{student['name']} is in {student['house']}")
#------------------------

# students = []
    
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# def get_name(student):
#     return student["name"]

# for student in sorted(students, key=get_name):
#     print(f"{student['name']} is in {student['house']}")
#-------------


# students = []
    
# with open("students.csv") as file:
#     for line in file:
#       name, house= line.rstrip().split(",")
#       student = {"name": name, "house": house}
#       students.append(student)

# for student in sorted(students, key=lambda student: student["name"]):
#    print(f"{student['name']} is in {student['house']}")
#-------------------------------

# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         students.append({"name": row[0], "home": row[1]})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

#------------------------
# import csv

# students = []
    
# with open("students.csv") as file:
#   reader = csv.reader(file)
#   for name, home in reader:
#      students.append({"name": name, "home": home})


# for student in sorted(students, key=lambda student: student["name"]):
#    print(f"{student['name']} is from {student['home']}")

#-------------------

import csv

students = []
    
with open("students.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
     students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
   print(f"{student['name']} is from {student['home']}")