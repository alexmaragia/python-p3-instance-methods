#!/usr/bin/env python3

class Person:
    # Instance Method to make the person talk
    def talk(self):
        print("Hello World!")

    # Instance Method to make the person walk
    def walk(self):
        print("The person is walking.")


# Creating instances to verify behavior
if __name__ == "__main__":
    john = Person()
    john.talk()  # Output: Hello World!
    john.walk()  # Output: The person is walking.

    jane = Person()
    jane.talk()  # Output: Hello World!
    jane.walk()  # Output: The person is walking.
