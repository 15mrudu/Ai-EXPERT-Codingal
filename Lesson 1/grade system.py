marks = int(input("Enter your marks: "))

# Check the grade
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

# Display the grade
print("Your grade is:", grade)

print("Congratulations! You completed the Grade System activity! ")