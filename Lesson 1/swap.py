num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Before swapping:")
print("First number:", num1)
print("Second number:", num2)

# Swap using temporary variable
temp = num1
num1 = num2
num2 = temp

print("\nAfter swapping:")
print("First number:", num1)
print("Second number:", num2)

print("\nCongratulations! You successfully swapped the numbers! ")