
# try:
#   x = int(input("What's x? "))
#   print(f"x is {x}")
# except ValueError:
#   print("x is not a number")


#   try:
#     x = int(input("What's x? "))
#   except ValueError:
#     print("x is not a number")
#   else:
#     print(f"x is {x}")

# while True:
#   try:
#     x = int(input("What's x? "))
#   except ValueError:
#     print("x is not a number")
#   else:
#     break

# print(f"x is {x}")

# while True:
#   try:
#     x = int(input("What's x? "))
#     break
#   except ValueError:
#     print("x is not a number")

# print(f"x is {x}")

# def main():
#   x = get_int()
#   print(f"x is {x}")

# def get_int():
#   while True:
#     try:
#       return int(input("What's x? "))
#     except ValueError:
#       print("x is not a number")

# Does not return an error message
# def get_int():
#   while True:
#     try:
#       return int(input("What's x? "))
#     except ValueError:
#       pass

# def main():
#   x = get_int("What is x? ")
#   print(f"x is {x}")

# def get_int(prompt):
#   while True:
#     try:
#       return int(input(prompt))
#     except ValueError:
#       pass

# Get integer code:

def main():
  x = get_int("What is x? ")
  print(f"x is {x}")

def get_int(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      print("Not a number")
      # pass



main()