score = int(input("Score: "))


# Option 1: 

# if score >= 90 and score <=100:
#     print("Grade A")
# elif score >= 80 and score < 90:
#     print("Grade: B ")
# elif score >= 70 and score <80:
#     print("Grade C")
# elif score >= 60 and score <70:
#     print("Grade D ")
# else:
#     print("Grade: F")

# Option 2: 

# if 90 <= score and score <=100:
#     print("Grade A")
# elif 80 <= score and score < 90:
#     print("Grade: B ")
# elif 70 <= score and score < 80:
#     print("Grade C")
# elif 60 <= score and score < 70:
#     print("Grade D ")
# else:
#     print("Grade: F")

# Option 3: 

# if 90 <= score <=100:
#     print("Grade A")
# elif 80 <= score < 90:
#     print("Grade: B ")
# elif 70 <= score < 80:
#     print("Grade C")
# elif 60 <= score < 70:
#     print("Grade D ")
# else:
#     print("Grade: F")

# Option 4:

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade: B ")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D ")
else:
    print("Grade: F")