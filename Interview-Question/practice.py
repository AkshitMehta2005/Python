class Student:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

        print("Hello World")
        print("Name:", self.name)
        print("Age:", self.age)

    # Method
    def add(self, a, b):
        print("Addition:", a + b)


# Create object
s1 = Student("Akshit", 21)

# Call method
s1.add(1, 2)