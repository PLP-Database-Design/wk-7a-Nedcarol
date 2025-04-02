def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, it is applied; otherwise, the original price is returned.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    return price

# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate and print final price
    final_price = calculate_discount(price, discount_percent)
    print(f"Final price after discount (if applicable): ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")
