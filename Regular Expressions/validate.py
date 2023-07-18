import re

email = input("What's your email? ").strip()

# if "@" in email and ". in email":
#     print("Valid")
# else:
#     print("Invalid")
#------------------------------
# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")
#---------------------------

# if re.search(".+@.+", email):
# if re.search(r"^.+@.+\.edu$", email):
# if re.search(r"^[^@]+@[^@]\.edu$", email):
# if re.search(r".+@.+", email):
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
# if re.search(r"^\w+@\w+\.edu$", email.lower):
# if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
# if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


#  . any character except a newline
#  * 0 or more repetitions
#  + 1 or more repititions
#  ? 0 or 1 repetitions
#  {x} x repetitions
# {x,y} x  
#------
#  \d  - Decimal Digit
#  \D  - Not a decimal digit
#  \s  - whitespace characters
#  \S  - not a whitespace character
#  \w  - word character... as well as numbers and the underscore
#  \W  - not a word caracter