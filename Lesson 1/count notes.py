# Ask the user to enter an amount
amount = int(input("Enter the amount: "))

# Count the number of 500 notes
notes_500 = amount // 500
amount = amount % 500

# Count the number of 200 notes
notes_200 = amount // 200
amount = amount % 200

# Count the number of 100 notes
notes_100 = amount // 100
amount = amount % 100

# Count the number of 50 notes
notes_50 = amount // 50
amount = amount % 50

# Count the number of 20 notes
notes_20 = amount // 20
amount = amount % 20

# Count the number of 10 notes
notes_10 = amount // 10
amount = amount % 10

# Display the result
print("\nNumber of notes:")
print("₹500 notes:", notes_500)
print("₹200 notes:", notes_200)
print("₹100 notes:", notes_100)
print("₹50 notes:", notes_50)
print("₹20 notes:", notes_20)
print("₹10 notes:", notes_10)

print("\nCongratulations! You successfully counted the notes! ")