"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from random import choice


class GenericNamer:
    """The GenericNamer is a class that allows for generation of names. It's up
       to the calling client to check for uniqueness.  New entities (offspring) 
       are named with the same names, but  with an added number to designate
       the generation
    """

    def __init__(self):
        self.descriptors = [
            "chunky",
            "buttery",
            "delicious",
            "scruptious",
            "dinosaur",
            "boopy",
            "lovely",
            "carniverous",
            "hanky",
            "loopy",
            "doopy",
            "astute",
            "gloopy",
            "outstanding",
            "stinky",
            "conspicuous",
            "fugly",
            "frigid",
            "angry",
            "adorable",
            "sticky",
            "moolicious",
            "cowy",
            "spicy",
            "grated",
            "crusty",
            "stanky",
            "blank",
            "bumfuzzled",
            "fuzzy",
            "hairy",
            "peachy",
            "tart",
            "creamy",
            "arid",
            "strawberry",
            "butterscotch",
            "wobbly",
            "persnickety",
            "nerdy",
            "dirty",
            "placid",
            "bloated",
            "swampy",
            "pusheena",
            "hello",
            "goodbye",
            "milky",
            "purple",
            "rainbow",
            "bricky",
            "muffled",
            "anxious",
            "misunderstood",
            "eccentric",
            "quirky",
            "lovable",
            "reclusive",
            "faux",
            "evasive",
            "confused",
            "crunchy",
            "expensive",
            "ornery",
            "fat",
            "phat",
            "joyous",
            "expressive",
            "psycho",
            "chocolate",
            "salted",
            "gassy",
            "red",
            "blue",
        ]

        self.nouns = [
            "squidward",
            "hippo",
            "butter",
            "animal",
            "peas",
            "lettuce",
            "carrot",
            "onion",
            "peanut",
            "cupcake",
            "muffin",
            "buttface",
            "leopard",
            "parrot",
            "parsnip",
            "poodle",
            "itch",
            "punk",
            "kerfuffle",
            "soup",
            "noodle",
            "avocado",
            "peanut-butter",
            "latke",
            "milkshake",
            "banana",
            "lizard",
            "lemur",
            "lentil",
            "bits",
            "house",
            "leader",
            "toaster",
            "signal",
            "pancake",
            "kitty",
            "cat",
            "cattywampus",
            "poo",
            "malarkey",
            "general",
            "rabbit",
            "chair",
            "staircase",
            "underoos",
            "snack",
            "lamp",
            "eagle",
            "hobbit",
            "diablo",
            "earthworm",
            "pot",
            "plant",
            "leg",
            "arm",
            "bike",
            "citrus",
            "dog",
            "puppy",
            "blackbean",
            "ricecake",
            "gato",
            "nalgas",
            "lemon",
            "caramel",
            "fudge",
            "cherry",
            "sundae",
            "truffle",
            "cinnamonbun",
            "pastry",
            "egg",
            "omelette",
            "fork",
            "knife",
            "spoon",
            "salad",
            "train",
            "car",
            "motorcycle",
            "bicycle",
            "platanos",
            "mango",
            "taco",
            "pedo",
            "nunchucks",
            "destiny",
            "hope",
            "despacito",
            "frito",
            "chip",
        ]

    def _generate(self, delim="-", length=4):
        """Generate a dino name. Inspiration from Haikunator, but much more
           poorly implemented ;) We also don't allow for use of any descriptor
           or noun more than once.
        """
        descriptor = self.select(self.descriptors)
        noun = self.select(self.nouns)
        return delim.join([descriptor, noun])

    def generate(self, delim="-"):
        return self._generate(delim)

    def select(self, select_from):
        """ select an element from a list using random.choice
        
            Parameters
            ==========
            should be a list of things to select from
        """
        if len(select_from) <= 0:
            return ""

        return choice(select_from)
