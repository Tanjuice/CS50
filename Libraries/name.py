import sys

# try:
#   print("Hello, my name is", sys.argv[1])
# except IndexError:
#   print("Too few arguments")



# Running command in command line + another string

# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

for arg in sys.argv[1:]:

# Print name tag
    # print("Hello, my name is", sys.argv[1])
    print("Hello, my name is", arg)
print("!?")