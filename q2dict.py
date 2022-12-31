
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

# delete the keys from the dictionary
for i in keys:
  sample_dict.pop(i, None)

print(sample_dict)