# Function that creates final price after applying a discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price
    
# User Input
original_price = float(input("Enter Original Price of item: "))
discount_per = float(input("Enter discount %: "))

# Print Output
print("Final Price is: ", calculate_discount(original_price, discount_per))