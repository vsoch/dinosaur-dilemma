"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from itertools import chain
from dinolemma.dinosaurs import Dinosaurs
from dinolemma.avocados import AvocadoTrees
import random
import numpy
import sys


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
        grid_size=25,
    ):

        # Start in a season to determine the weather
        self.days_in_season = days_in_season
        self.season = random.choice(["summer", "spring", "winter", "fall"]) or season
        self.days_left_season = (
            random.choice(range(self.days_in_season)) or days_left_season
        )

        # Simulation parameters
        self.grid_size = grid_size

        # Create a set of dinosaurs and avocado trees
        self.dinosaurs = Dinosaurs(number_dinos)
        self.trees = AvocadoTrees(number_trees)

        # Initialize the grid, place dinos and others on it
        self._init_grid()

        # Progress the first day to set temperature, etc.
        self.newday()

    def summary(self):
        """Print a summary of the season, day, and general weather for the 
           simulation
        """
        print(
            "Today is day %s in the %s season." % (self.days_left_season, self.season)
        )
        print(
            "There are %s dinosaurs, and %s avocado trees."
            % (self.dinosaurs.count, self.trees.count)
        )
        print("The temperate is %s°F, humidity %s" % (self.temperature, self.humidity))

    # Grid and movement

    def _init_grid(self):
        """Initialize the grid, meaning creating it, ensuring it's large 
           enough, and placing dinosaurs and avocado trees on it
        """
        # Initialize a grid for the simulation (empty is None)
        self.grid = numpy.empty(shape=(self.grid_size, self.grid_size), dtype=object)
        choices = [x[0] for x in list(numpy.ndenumerate(self.grid))]
        random.shuffle(choices)

        # We must have enough spots on the grid, should be 10 more
        if self.dinosaurs.count + self.trees.count + 10 > len(choices):
            sys.exit("You must increase grid size or decrease entities.")

        # Allocate each a location on the grid
        for entity in chain(self.dinosaurs, self.trees):
            x, y = choices.pop()
            self.move(entity, x, y)

    def move(self, entity, x, y):
        """Handle assigning an entity to a new spot, along with assigning the
           entity name to the spot
        """
        # Clear the previous position
        if entity.on_grid:
            self.grid[entity.x, entity.y] = None

        # Set the new location
        entity.set_location(x, y)
        self.grid[x, y] = entity.name

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
        self.humidity = numpy.random.choice(
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
        self.summary()
