#number = 9

#if number > 10:
#    print("number is greater than 10")
#else:
#    print("number is less than 10")

#age = 18

#if age >= 18:
#    print("you are eligible for vote")
#else:
#    print("you are not eligible for vote")

age = 18
gender = "female"
weight = 60
if age >= 18:
    if(gender == "male" and weight >= 50) or (gender == "female" and weight >= 60):
        print("You are eligible for blood donate")
    else:
        print("You are not eligible for blood donate")
else:
    print("You are not eligible for blood donate")
