"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from dinolemma.namer import GenericNamer
import random


class Entity:
    """An Entity is a base class for a living thing in the world.
    """

    def __init__(self, name):
        self.name = name

    def set_location(self, x, y):
        """set an entity location on the board - an x and y coordinate
        """
        self.x = x
        self.y = y

    @property
    def on_grid(self):
        """An entity with an x and y coordinate is assumed to be on the grid
        """
        if hasattr(self, "x") and hasattr(self, "y"):
            return True
        return False


class Group:
    """A group is a generic base class to hold a group of entities.
       An implementing subclass should add a name (e.g., dinosaurs) along
       with a class of entity to implement (e.g., Dinosaur). Custom functions 
       for interaction based on the names of other groups.
    """

    def __init__(self, name, Entity, number=None, namer=None):
        number = number or random.choice(range(15))
        self.entities = []
        namer = namer or GenericNamer
        self.namer = namer()
        self.name = name

        names = []
        for _ in range(number):
            name = self.namer.generate()

            # Keep generating name until we get a unique one
            while name in names:
                name = self.namer.generate()

            names.append(name)
            self.entities.append(Entity(name))

    @property
    def count(self):
        return len(self.entities)

    def __str__(self):
        return "[%s %s]" % (self.count, self.name)

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        for entity in self.entities:
            yield entity
