#!/usr/bin/env python3
"""
This module demonstrates the use of mixins to add reusable behavior
to a class without requiring inheritance from unrelated classes.

It defines two mixins, SwimMixin and FlyMixin, which provide
swim and fly abilities. These are then used in the Dragon class,
which combines both abilities and adds its own specific behavior.
"""


class SwimMixin:
    """
    SwimMixin provides swimming capability to any class that inherits from it.

    Methods:
        swim(): Prints a message indicating the creature is swimming.
    """

    def swim(self):
        """Print a message indicating that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """
    FlyMixin provides flying capability to any class that inherits from it.

    Methods:
        fly(): Prints a message indicating the creature is flying.
    """

    def fly(self):
        """Print a message indicating that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class inherits from SwimMixin and FlyMixin.

    It combines swimming, flying, and its own unique behavior: roaring.

    Methods:
        roar(): Prints a message indicating that the dragon roars.
    """

    def roar(self):
        """Print a message indicating that the dragon roars."""
        print("The dragon roars!")
