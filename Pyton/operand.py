def task2(operand1, operator, operand2):
  """
  Performs an arithmetic operation based on the given operator and operands.

  Args:
      operand1: The first operand (can be a string or a number).
      operator: The arithmetic operator (+, -, *, /).
      operand2: The second operand (can be a string or a number).

  Returns:
      The result of the arithmetic operation, or an error message if the operation is invalid.
  """

  try:
    # Convert operands to numbers if they are strings
    if isinstance(operand1, str):
      operand1 = float(operand1)
    if isinstance(operand2, str):
      operand2 = float(operand2)

    # Perform the arithmetic operation based on the operator
    if operator == "+":
      result = operand1 + operand2
    elif operator == "-":
      result = operand1 - operand2
    elif operator == "*":
      result = operand1 * operand2
    elif operator == "/":
      if operand2 == 0:
        raise ZeroDivisionError("Division by zero")
      result = operand1 / operand2
    else:
      raise ValueError("Invalid operator")

  except (TypeError, ValueError) as e:
    result = f"Error: {e}"

  return result

# Test cases
print(task2(10, "+", 5))  # Output: 15
print(task2(10, "-", 5))  # Output: 5
print(task2("10", "*", 5))  # Output: 50
print(task2("10", "/", "5"))  # Output: 2.0
print(task2("5", "-", 10))  # Output: -5.0
print(task2(10, "x", 5))  # Output: Error: Invalid operator
