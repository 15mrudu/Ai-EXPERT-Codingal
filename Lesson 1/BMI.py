# Ask for weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height * height)

print("Your BMI is:", bmi)

# Use AND operator
if bmi >= 18.5 and bmi < 25:
    print("You have a normal BMI.")

# Use OR operator
elif bmi < 18.5 or bmi >= 25:
    print("Your BMI is outside the normal range.")

# Use NOT operator
if not bmi < 18.5:
    print("Your BMI is not in the underweight range.")

print("Congratulations! You completed the BMI activity! ")