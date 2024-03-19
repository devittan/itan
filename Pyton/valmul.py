def task4(value, multiplier):
   """
   Returns either a string repeated X times or the product of two numbers (the arithmetic operation).
   Returns False if the second argument is NOT a number.
   """

   try:
       # Attempt to multiply them as numbers
       result = value * multiplier
   except TypeError:
       # If multiplication fails, treat them as strings
       if isinstance(multiplier, int):
           # Repeat the string if the multiplier is an integer
           result = value * multiplier
       else:
           # Return False if the multiplier is not a number
           result = False

   return result
# Test cases (with expected outputs)
print(task4("hello", 3))  # Output: hellohellohello
print(task4(10, 3))       # Output: 30
print(task4("10", 3))      # Output: 101010
print(task4("10", "3"))    # Output: False
print(task4("hi", "2"))    # Output: False