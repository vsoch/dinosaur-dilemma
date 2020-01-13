"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from dinolemma.entity import Group, Entity
from dinolemma.namer import GenericNamer
import random


class AvocadoTree(Entity):
    def __init__(self, name):
        super().__init__(name=name)

        # The age of an avocado tree is represented by it's height
        self.height = random.choice(range(100)) * 0.01

    def grow(self):
        """If the avocado tree is less than it's full size, allow it to grow.
           The growth is an equation of the current sunlight and water 
           conditions.
        """
        # TODO: need to add humidity and temperature here.
        if self.height < 1.0:
            self.height += 0.01


class AvocadoNamer(GenericNamer):
    """The AvocadoNamer subclasses a GenericNamer, but adds a tree extension
    """

    def __str__(self):
        return "[avocado-namer]"

    def __repr__(self):
        return self.__str__()

    def generate(self, delim="-"):
        prefix = self._generate(delim)
        return "%s%stree" % (prefix, delim)


class AvocadoTrees(Group):
    """A group of avocado trees
    """

    def __init__(self, number=None):
        super().__init__(
            name="trees", number=number, Entity=AvocadoTree, namer=AvocadoNamer
        )
