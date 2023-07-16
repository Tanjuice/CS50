# names = []

# for _ in range(3):
#   names.append(input("What's your name? "))
#   # name = input("What's your name? ")
#   # names.append(name)

# for name in sorted(names):
#   print(f"hello, {name}")

#---------------
# name = input("What's your name? ")

# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close

# with open("names.txt", "a") as file:
#   file.write(f"{name}\n")

#---------------

# with open("names.txt", "r") as file:
# #     lines = file.readlines()

# # for line in lines:
# #     print("Hello", line.rstrip())

#   for line in file:
#     print("Hello,", line.rstrip())

#-----------------
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=False):
    print(f"Hello, {name}")

#-----------------------

# with open("names.txt") as file:
#     for line in sorted(file):
#         print("Hello, ", line.rstrip())