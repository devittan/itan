def calculate_sales_tax(total):
    """Calculates the sales tax based on the given total."""
    tax_rate = 0.06  # 6% sales tax rate
    sales_tax = round(total * tax_rate, 2)
    return sales_tax

def calculate_total_after_tax(total):
    """Calculates the total after tax based on the given total."""
    sales_tax = calculate_sales_tax(total)
    return round(total + sales_tax, 2)