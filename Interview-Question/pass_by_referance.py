# List, dictionary, set → mutable → changes can affect the original object.
# int, float, str, tuple → immutable → assigning a new value inside the function doesn't change the original object.

def add_item(x):
    x.append("Apple")

fruits = ["Mango", "Banana"]

add_item(fruits)

print(fruits)