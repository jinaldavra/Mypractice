# x = 75

# if x > 90:
#     grade = 'A'
# elif x > 80:
#     grade = 'B'
# elif x > 70:
#     grade = 'C'
# elif x > 60:
#     grade = 'D'
# else:
#     grade = 'F'

# print(f"Your grade is {grade}")

temperature = float(input("Enter the temperature in Celsius : "))

if temperature > 37.5:
    print("You have a fever")
elif temperature > 35.5:
    print("Your temperature is normal")
else:
    print("You are hypothermic")