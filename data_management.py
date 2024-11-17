import sys

try:
  a = float(sys.argv[1]) 
  b = float(sys.argv[2])
  c = float(sys.argv[3])
  d = float(sys.argv[4])
  e = float(sys.argv[5])
except ValueError:
  print("<span style='color: red;'>Error message: All values must be numeric</span>")
  sys.exit()

numbers = [a, b, c, d, e]

if any(number < 0 for number in numbers):
  print("<span style='color: red;'>Error message: Negative values are not allowed.</span>")
else:
  average = sum(numbers) / len(numbers)
  
  if average > 50:
    print(f"<p>Average of numbers is <span style='color: green;'>{average}</span> and <span style='color: green;'>greater than 50<span></p>")
  else:
    print(f"<p>Average of numbers is <span style='color: green;'>{average}</span> and <span style='color: green;'>less or equal than 50</span></p>")

  positive_count = len([number for number in numbers if number > 0])

  if positive_count & 1 == 0:
    even_odd = "even"
  else:
    even_odd = "odd"

  print(f"<p>The count of positive numbers is <span style='color: green;'>{even_odd}</span></p>")

  greater_than_ten = sorted([number for number in numbers if number > 10])

  original_values = ", ".join(map(str, numbers))
  sorted_values = ", ".join(map(str, greater_than_ten))

  html_output = (
    f"<p>Original values: <span style='color: green;'>{original_values}</span></p>"
    f"<p>Values greater than 10: <span style='color: green;'>{sorted_values}</span></p>"
  )

  print(html_output)