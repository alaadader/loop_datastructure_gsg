
number = 76542
reversed_number = 0

while number > 0:
  # extract the last digit of the number
  last_digit = number % 10
  # append the last digit to the reversed number
  reversed_number = reversed_number * 10 + last_digit
  # remove the last digit from the number
  number //= 10

print("the reversed for 76542 is",reversed_number)  # prints 24567
