"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""


from .namer import GenericNamer
import random


class Dinosaur:
    def __init__(self, name):

        self.name = name

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


class Dinosaurs:
    """A group of dinosaurs
    """

    def __init__(self, number=None):
        number = number or random.choice(range(15))
        self.dinosaurs = []
        self.namer = DinosaurNamer()

        for _ in range(number):
            name = self.namer.generate()
            self.dinosaurs.append(Dinosaur(name))

    def __str__(self):
        return "[%s dinosaurs]" % len(self.dinosaurs)

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        for dinosaur in self.dinosaurs:
            yield dinosaur


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

    def generate(self, delim="-"):
        prefix = self._generate(delim)
        suffix = self.select(self.suffix)
        return "%s%s" % (prefix, suffix)
