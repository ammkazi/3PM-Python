# Parent Class
class Animal:

    def sound(self):
        print("Animal makes a sound")


# Child Class
class Dog(Animal):

    def sound(self):
        print("Dog barks")


# Creating object
d1 = Dog()

d1.sound()