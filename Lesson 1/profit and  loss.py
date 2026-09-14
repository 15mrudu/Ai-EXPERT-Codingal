# Ask for cost price and selling price
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

# Check profit or loss
if selling_price > cost_price:
    profit = selling_price - cost_price
    print("You made a profit of:", profit)

elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("You made a loss of:", loss)

else:
    print("There is no profit and no loss.")

# Congratulations message
print("\nCongratulations! You successfully completed the Profit and Loss activity! ")