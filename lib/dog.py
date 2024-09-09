#!/usr/bin/env python3

class Dog:
    # Instance Method to make the dog bark
    def bark(self):
        print("Woof!")

    # Instance Method to make the dog sit
    def sit(self):
        print("The dog is sitting.")


# Creating instances to verify behavior
if __name__ == "__main__":
    fido = Dog()
    fido.bark()  # Output: Woof!
    fido.sit()   # Output: The dog is sitting.

    snoopy = Dog()
    snoopy.bark()  # Output: Woof!
    snoopy.sit()   # Output: The dog is sitting.
