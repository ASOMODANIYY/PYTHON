def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price
    original_price = float(input("Enter the original price: "))
    dicount_percent = float(input("Enter the discount percentage: "))
    calculate_discount(original_price, dicount_percent)
    print(f"The final price is: ${final_price: .2f}")