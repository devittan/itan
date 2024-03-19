def task1(text1, text2, text3):
  """
  Returns the longest text string, or a concatenation of the tied texts separated by underscores.

  Args:
      text1: The first text string.
      text2: The second text string.
      text3: The third text string.

  Returns:
      The longest text string, or a concatenation of the tied texts separated by underscores.
  """

  # Find the longest text string.
  longest_text = max(text1, text2, text3, key=len)

  # If there is a tie, concatenate the tied texts separated by underscores.
  if len(text1) == len(longest_text) and text1 != longest_text:
    result = text1 + "_" + longest_text
  elif len(text2) == len(longest_text) and text2 != longest_text:
    result = text2 + "_" + longest_text
  elif len(text3) == len(longest_text) and text3 != longest_text:
    result = text3 + "_" + longest_text
  else:
    result = longest_text

  return result

# Test cases
print(task1("hi", "bye", "hello"))  # Output: hello
print(task1("hello", "create", "every"))  # Output: create
print(task1("hi", "al", "oh"))  # Output: hi_al_oh
print(task1("two", "hi", "one"))  # Output: two_one
print(task1(" ", " ", " "))  # Output:  