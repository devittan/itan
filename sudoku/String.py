import math

def greeting(name):
  """
  Greets the customer with a personalized message.
  """
  print(f"Hello, {name}! Welcome to the Painting Room Calculator.")

def calculate_print_price():
  """
  Calculates the number of gallons of paint needed and expected price.
  """
  # Get paint information
  sq_ft_per_gallon = float(input("Enter the square footage covered by one gallon of paint: "))
  price_per_gallon = float(input("Enter the price per gallon of paint: $"))

  # Get room dimensions
  length = float(input("Enter the room length (ft): "))
  width = float(input("Enter the room width (ft): "))
  height = float(input("Enter the wall height (ft): "))

  # Calculate surface area
  surface_area = 2 * (length * height) + 2 * (width * height)
  print(f"The room surface area is {surface_area:.2f} square feet.")

  # Calculate number of gallons required
  gallons_needed = math.ceil(surface_area / sq_ft_per_gallon)
  print(f"You will need approximately {gallons_needed} gallons of paint.")

  # Calculate expected purchase price
  expected_price = gallons_needed * price_per_gallon
  print(f"The expected cost of paint is ${expected_price:.2f}.")

# Main program
name = input("Enter your name: ")
greeting(name)
calculate_print_price()

print("\nThank you for using the Painting Room Calculator!")
