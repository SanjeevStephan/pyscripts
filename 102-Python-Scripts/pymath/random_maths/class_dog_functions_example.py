# Defining a Class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

# Creating an object of the class Dog
my_dog = Dog("Buddy", 5)

# Accessing attributes of the object
print("My dog's name is", my_dog.name)
print("My dog's age is", my_dog.age)

# Calling the bark method of the object
my_dog.bark()