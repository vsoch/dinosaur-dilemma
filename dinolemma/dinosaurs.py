"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""


from dinolemma.entity import Group, Entity
from dinolemma.namer import GenericNamer
import random


class Dinosaur(Entity):
    def __init__(self, name):
        super().__init__(name=name)

        # Baby dinosaurs don't exist, they just get large enough
        self.size = random.choice(range(100)) * 0.01

        # 0 is ravenous (dead) 1 is full. We start out satiated
        self.hunger = random.choice(range(80, 100)) * 0.01

    @property
    def is_mature(self):
        """determine if a dinosaur is mature, greater than or == 80% of full
           size, whatever unit that happens to be.
        """
        return self.size >= 0.8


class DinosaurNamer(GenericNamer):
    """The DinosaurNamer subclasses a GenericNamer, but adds a dinosaur extension
       to complete the name.
    """

    def __init__(self):

        self.suffix = [
            "asaurus",
            "isaurus",
            "iraptor",
            "raptor",
            "us",
            "docus",
            "podus",
        ]
        super().__init__()

    def __str__(self):
        return "[dinosaur-namer]"

    def __repr__(self):
        return self.__str__()

    def generate(self, delim="-"):
        prefix = self._generate(delim)
        suffix = self.select(self.suffix)
        return "%s%s" % (prefix, suffix)


class Dinosaurs(Group):
    """A group of dinosaurs
    """

    def __init__(self, number=None):
        super().__init__(
            name="dinosaurs", number=number, Entity=Dinosaur, namer=DinosaurNamer
        )
