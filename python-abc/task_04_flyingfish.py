#!/usr/bin/env python3
"""
This module demonstrates multiple inheritance in Python using three classes:
Fish, Bird, and FlyingFish.

Each class provides methods representing animal behavior and habitat.
The FlyingFish class inherits from both Fish and Bird, and overrides their
methods.
It also includes an example of the method resolution order (MRO).
"""


class Fish:
    """
    Fish class represents a general fish.

    Methods:
        swim(): Prints that the fish is swimming.
        habitat(): Prints that the fish lives in water.
    """

    def swim(self):
        """Print a message indicating that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print the natural habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """
    Bird class represents a general bird.

    Methods:
        fly(): Prints that the bird is flying.
        habitat(): Prints that the bird is flying (possibly an error).
    """
    def fly(self):
        """Print a message indicating that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print the natural habitat of the bird
        (seems to repeat fly message.)"""
        print("The bird is flying")


class FlyingFish(Fish, Bird):
    """
    FlyingFish class demonstrates multiple inheritance from Fish and Bird.

    Methods override those of parent classes to reflect unique behavior.
    """

    def fly(self):
        """Print a message indicating that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print a message indicating that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the unique habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")


def __MRO__(self):
    """
    Demonstrate the use of FlyingFish class and display its method
    resolution order (MRO).

    This function calls swim, fly, habitat on a FlyingFish instance,
    and prints the MRO list.
    """
    FlyingFish().swim()
    FlyingFish().fly()
    FlyingFish().habitat()
    print(FlyingFish.mro())
