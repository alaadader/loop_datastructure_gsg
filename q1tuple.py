tuple1 = (10, 20, 30, 40, 50)

# create an empty list
reversed_list = []

# reverse the tuple using a loop
for i in range(len(tuple1)):
  reversed_list.append(tuple1[len(tuple1) - i - 1])

# create a new tuple from the reversed list
reversed_tuple = tuple(reversed_list)

print(reversed_tuple)  # prints (50, 40, 30, 20, 10)
