"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from dinolemma.namer import GenericNamer
import random


class Entity:
    """An Entity is a base class for a living thing in the world. An entity
       that can move is allowed to change location on the grid.
    """

    def __init__(self, name, can_move=True):
        self.name = name
        self.can_move = can_move

    def __str__(self):
        return "[%s: %s]" % (self.__class__.__name__, self.name)

    def set_location(self, x, y):
        """set an entity location on the board - an x and y coordinate
        """
        self.x = x
        self.y = y

    def interact(self, entity):
        """Given a second entity, based on its type, interact with it.
        """
        print("%s is interacting with %s" % (self, entity))

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
        self.entities = {}
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
            self.entities[name] = Entity(name)

    @property
    def count(self):
        return len(self.entities)

    def random(self):
        """Randomly select an entity"""
        if len(self.entities) > 0:
            return random.choice(list(self.entities.values()))

    def __str__(self):
        return "[%s %s]" % (self.count, self.name)

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, key):
        if key in self.entities:
            return self.entities[key]

    def __iter__(self, randomize=True):
        """iterator over entities. By default, we randomize the order
        """
        entities = list(self.entities.keys())
        if randomize:
            random.shuffle(entities)
        for name in entities:
            yield self.entities[name]
