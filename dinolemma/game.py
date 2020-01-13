"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

import random
import numpy


class DinosaurDilemma:
    """A dinosaur dilemma simulation contains basic variables to control
       the environment (season, climate) along with probabilities
       for events. Largely, if values are undefined, they are randomly
       selected from within some range.
    """

    def __init__(
        self,
        days_left_season=None,
        season=None,
        days_in_season=90,
        number_dinos=None,
        number_trees=None,
    ):

        # Start in a season to determine the weather
        self.days_in_season = days_in_season
        self.season = random.choice(["summer", "spring", "winter", "fall"]) or season
        self.days_left_season = (
            random.choice(range(self.days_in_season)) or days_left_season
        )

        # Initialize a grid for the simulation
        self.grid = []  # TODO

        # Create a set of dinosaurs and avocado trees
        self.dinosaurs = Dinosaurs(number_dinos)
        self.trees = AvocadoTrees(number_trees)

        # Progress the first day to set temperature, etc.
        self.newday()

    def summary(self):
        """Print a summary of the season, day, and general weather for the 
           simulation
        """
        # today is day ___ in the ___ season
        # there are ___ dinosaurs and ___ avocado trees

    # Climate

    def set_climate(self):
        """Set the climate, meaning the temperature (depending on the season)
           and the humidity (also largely depending on the season
        """
        chance_humid = 0.5
        if self.season == "winter":
            self.temperature = random.choice(range(0, 32))
            chance_humid = 0.1
        elif self.season == "fall":
            self.temperature = random.choice(range(30, 62))
            chance_humid = 0.6
        elif self.season == "spring":
            self.temperature = random.choice(range(40, 55))
            chance_humid = 0.4
        elif self.season == "summer":
            self.temperature = random.choice(range(56, 89))
            chance_humid = 0.75
        self.set_humidity(chance_humid)

    def set_humidity(self, chance_humid):
        """Determine the humidity, a percentage value.
        """
        low_humidity = random.choice(range(30, 50)) * 0.01
        high_humidity = random.choice(range(50, 80)) * 0.01
        return numpy.random.choice(
            [low_humidity, high_humidity], p=[1 - chance_humid, chance_humid]
        )

    # Time

    def next_season(self):
        """return the next season"""
        return {
            "summer": "fall",
            "fall": "winter",
            "winter": "spring",
            "spring": "summer",
        }[self.season]

    def newday(self):
        """For each new day, these is a different value for water and sunlight,
           depending on the season.
        """
        # 1. Adjust day and season, and climate
        if self.days_left_season == 1:
            self.season = self.next_season()
            self.days_left_season = 90

        self.set_climate()
