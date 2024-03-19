def findMax(num_list):
  """
  This function finds the index of the largest value in a list of numbers.

  Args:
    num_list: A list of numbers.

  Returns:
    The index of the largest value in the list.
  """
  max_value = num_list[0]
  max_index = 0
  for i in range(1, len(num_list)):
    if num_list[i] > max_value:
      max_value = num_list[i]
      max_index = i
  return max_index

def evenOrOdd(num_list, string_list):
  """
  This function checks each number in a list and places "even" or "odd" in a corresponding string list.

  Args:
    num_list: A list of numbers.
    string_list: An empty list to store "even" or "odd" strings.
  """
  for num in num_list:
    if num % 2 == 0:
      string_list.append("even")
    else:
      string_list.append("odd")

# Create the number list and string list
num_list = [56, 77, 23, 12, 88, 59, 97, 33, 38, 64]
string_list = []

# Find the maximum value and index
max_index = findMax(num_list)
max_value = num_list[max_index]

# Check if even or odd and append to string list
evenOrOdd(num_list, string_list)

# Print the results
print(f"The largest value in the list is {max_value} located at index position {max_index}.")
print("The numbers were:")
for i in range(len(num_list)):
  print(f"Number {num_list[i]} is {string_list[i]}")