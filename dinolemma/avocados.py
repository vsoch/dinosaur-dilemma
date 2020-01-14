"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from dinolemma.entity import Group, Entity
from dinolemma.namer import GenericNamer
import random
import numpy


class AvocadoTree(Entity):
    def __init__(self, name, can_move=False):
        super().__init__(name=name, can_move=can_move)

        # The age of an avocado tree is represented by it's height
        self.height = random.choice(range(100)) * 0.01
        self.dead = False
        self.happy = True
        self.is_diseased = False

        # More than 80% grown, we can have avocados!
        self.avocados = 0
        if self.height > 0.80:
            self.avocados = random.choice(range(0, 5))

        # At this temperature, there is a 50% chance of freezing
        self.freezing_point = random.choice(range(-100, 32))

        # Probabilities are different per tree
        self.probability_disease = random.choice(range(0, 5)) * 0.01
        self.probability_reproduce = random.choice(range(0, 5)) * 0.01

    def stats(self):
        """Return stats for an avocado tree
         """
        stats = {"avocados": self.avocados, "height": self.height, "happy": self.happy}
        return stats

    @property
    def is_dead(self):
        """A dead avocado tree has size 0 or less, meaning it could have been
           stepped on, or destroyed/ eaten by a dinosaur
        """
        return self.height <= 0 or self.dead

    @property
    def is_mature(self):
        """A mature tree can reproduce
        """
        return self.height > 0.80

    def change(self, **kwargs):
        """If the avocado tree is less than it's full size, allow it to grow.
           The growth is an equation of the current sunlight and water 
           conditions.
        """
        # We should have all arguments, but good to be careful
        temperature = kwargs.get("temperature", 55)
        humidity = kwargs.get("humidity", 0.5)

        # Avocado trees grow well in higher humidity, moderate temperatures
        # A diseased tree cannot grow or reproduce
        self.happy = False
        if temperature > 40 and temperature < 65 and not self.is_diseased:
            self.height = max(1, self.height + numpy.power(humidity, 10))
            self.happy = True

        # Avocado Trees can freeze to death, moreso if they are diseased
        if temperature <= self.freezing_point:
            p = [0.5, 0.5] if self.is_diseased else [0.6, 0.4]
            self.dead = numpy.random.choice([True, False], p=p)

        # A healthy tree can get a disease (but can't get better)
        self.is_diseased = numpy.random.choice(
            [True, self.is_diseased],
            p=[self.probability_disease, 1 - self.probability_disease],
        )

        # Healthy avocado trees that are full grown can produce an avocado or grow!
        if not self.is_dead and not self.is_diseased:
            self.grow_avocado()

    def grow_avocado(self):
        """A healthy avocado tree can generate a new avocado!
        """
        if self.is_mature:
            self.avocados += numpy.random.choice(
                [0, random.choice(range(0, 5))], p=[0.2, 0.8]
            )

    def reproduce(self, **kwargs):
        """An avocado tree has a small percentage of reproducing if it's over
           a particular height (mature) and the weather is good.
        """
        if self.is_mature and self.happy:
            return numpy.random.choice(
                [True, False],
                p=[self.probability_reproduce, 1 - self.probability_reproduce],
            )
        return False


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
