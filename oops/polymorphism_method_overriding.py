# Method Overriding



# class Animal:

#     def sound(self):
#         print("Animal makes a sound")


# class Dog(Animal):

#     def sound(self):
#         print("Dog says: Bark")


# class Cat(Animal):

#     def sound(self):
#         print("Cat says: Meow")


# dog = Dog()
# cat = Cat()

# dog.sound()
# cat.sound()


# Method Overloading in Python

# Method overloading means having the same method name but different parameters, so the method can perform different operations depending on the arguments.
class Calculator:

    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
    
    
a = Calculator()
a.add(1,3)
a.add(1,1,1)
