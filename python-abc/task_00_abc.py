#!/usr/bin/env python3
"""
This module defines an abstract base class `Animal` and its concrete
subclasses.

The `Animal` class uses the `abc` module to enforce that all subclasses must
implement the `sound` method. This design ensures that any animal subclass
must provide its own implementation of how it sounds.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for animals.

    This class defines a contract that any subclass must
    implement the `sound` method.

    Methods:
        sound(): Abstract method to be implemented by all subclasses.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method that should be overridden to return the sound
        of the animal.

        Example:
        >>> class Horse(Animal):
        ...     def sound(self):
        ...         return "Neigh"
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal.

    Overrides the `sound` method to return the typical dog sound.
    """
    def sound(self):
        """
        Returns the sound a dog makes.

        Returns:
            str: The string "Bark"

        Example:
        >>> Dog().sound()
        'Bark'
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal.

    Overrides the `sound` method to return the typical cat sound.
    """
    def sound(self):
        """
        Returns the sound a cat makes.

        Returns:
            str: The string "Meow"

        Example:
        >>> Cat().sound()
        'Meow'
        """
        return "Meow"
