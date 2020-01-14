"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""


import random


def dinosaurXdinosaur(entity1, entity2):
    """A dinosaur by dinosaur interaction. The first (entity1) is the entity
       that has come upon the second (entity2) in the game
    """
    # TODO: define interactions
    print("%s is interacting with %s" % (entity1, entity2))


def dinosaurXavocado(dino, tree):
    """A dinosaur by avocado interaction, meaning that the dinosaur was moving
       and finds an avocado tree.
    """
    print("%s is interacting with %s" % (dino, tree))
