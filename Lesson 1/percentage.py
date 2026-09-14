
# Ask the user to enter marks
maths = float(input("Enter marks in Maths: "))
science = float(input("Enter marks in Science: "))
english = float(input("Enter marks in English: "))
computer = float(input("Enter marks in Computer: "))
social_science = float(input("Enter marks in Social Science: "))

# Calculate total marks
total = maths + science + english + computer + social_science

# Calculate percentage
percentage = (total / 500) * 100

# Display the result
print("\nResult")
print("Total marks:", total)
print("Percentage:", percentage, "%")

# Congratulations message
print("\nCongratulations! You successfully calculated your percentage! ")