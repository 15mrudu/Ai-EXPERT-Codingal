# Ask the user for two numbers
number = int(input("Enter a number: "))
divisor = int(input("Enter the number to divide by: "))

# Check divisibility
if number % divisor == 0:
    print(number, "is divisible by", divisor)
else:
    print(number, "is not divisible by", divisor)

# Congratulations message
print("Congratulations! You completed the Divisible Number activity! ")