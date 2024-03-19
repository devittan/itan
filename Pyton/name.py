def task3(name):
  """
  Determines if a name is valid. A valid name contains only one space and at least 5 characters.
  Punctuation marks are removed before validation.

  Args:
      name: The name to validate.

  Returns:
      True if the name is valid, False otherwise.
  """

  # Remove punctuation
  name_without_punctuation = ''.join(char for char in name if char.isalnum() or char.isspace())

  # Check if the name has at least 5 characters
  if len(name_without_punctuation) < 5:
    return False

  # Split the name by spaces and check if there is only one space
  words = name_without_punctuation.split()
  if len(words) != 2:
    return False

  # Check if each word contains only letters
  for word in words:
    if not word.isalpha():
      return False

  return True

# Test cases
print(task3("foo"))  # False
print(task3("having fun?"))  # True
print(task3("Python Rocks"))  # True
print(task3("Python is the best language"))  # False
print(task3("a b"))  # False