import sales_tax_calculator

def get_item_costs():
    """Gets the costs of items from the user."""
    items = []
    while True:
        cost = input("Cost of item (or 0 to end): ")
        if cost == "0":
            break
        items.append(float(cost))
    return items

def display_results(total, sales_tax, total_after_tax):
    """Displays the calculated results."""
    print("Total:           ${:.2f}".format(total))
    print("Sales tax:       ${:.2f}".format(sales_tax))
    print("Total after tax: ${:.2f}".format(total_after_tax))

def main():
    """Main function to drive the sales tax calculator."""
    while True:
        items = get_item_costs()
        total = sum(items)
        sales_tax = sales_tax_calculator.calculate_sales_tax(total)
        total_after_tax = sales_tax_calculator.calculate_total_after_tax(total)
        display_results(total, sales_tax, total_after_tax)

        again = input("Again? (y/n): ")
        if again.lower() != "y":
            break

    print("Thanks, bye!")

if __name__ == "__main__":
    main()