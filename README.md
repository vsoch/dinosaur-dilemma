# Dinosaur Dilemma

[![PyPI version](https://badge.fury.io/py/dinolemma.svg)](https://pypi.org/project/dinolemma/)
[![GitHub actions status](https://github.com/vsoch/dinosaur-dilemma/workflows/ci/badge.svg?branch=master)](https://github.com/vsoch/dinosaur-dilemma/actions?query=branch%3Amaster+workflow%3Aci)

![https://raw.githubusercontent.com/vsoch/dinosaur-dilemma/master/img/dinosaur-dilemma.gif](https://raw.githubusercontent.com/vsoch/dinosaur-dilemma/master/img/dinosaur-dilemma.gif)

This is the dinosaur dilemma, my first attempt at a simulation. It involves
characters, interactions, and variables that control those interactions.
The characters interact in a basic world and at the end, we are
interested to know how they turned out (evolved) given the parameters of the simulation. 
You can see a verbose text simulation run <a href="https://asciinema.org/a/293693" target="_blank"><img src="https://asciinema.org/a/293693.svg" />here</a>,
or a less verbose (text) run below:

[![asciicast](https://asciinema.org/a/293703.svg)](https://asciinema.org/a/293703)

A gif of the graphical interface to run the same simulation is shown above, and a static image below!

![https://raw.githubusercontent.com/vsoch/dinosaur-dilemma/master/img/dinosaur-dilemma.png](https://raw.githubusercontent.com/vsoch/dinosaur-dilemma/master/img/dinosaur-dilemma.png)

## Usage

### Install

You can install from pip, or directly from the repository here.

```bash
pip install dinolemma
```
or

```bash
git clone https://github.com/vsoch/dinosaur-dilemma
cd dinosaur-dilemma
python setup.py install
```

If you want to use the GUI you will need pygame. Any of the following will work.

```bash
pip install .[game]
pip install dinolemma[game]
pip install pygame
```

I find it very appropriate and lovely that the ubuntu icon for the pygame 
window is a tiny dinosaur :)

![https://raw.githubusercontent.com/vsoch/dinosaur-dilemma/master/img/pygame.png](https://raw.githubusercontent.com/vsoch/dinosaur-dilemma/master/img/pygame.png)

### Command

You can run a text simulation (with defaults) from the command line:

```bash
$ dinolemma run
Today is day 80 in the winter season.
There are 5 dinosaurs, and 13 avocado trees.
The temperate is 12°F, humidity 0.33
```

or a (more fun) graphical simulation (press enter to cycle through days):

```bash
dinolemma gui
```

The gui takes the same input parameters as the run.

```bash
dinolemma gui --help
usage: dinolemma gui [-h] [--ndinos NDINOS] [--ntrees NTREES]
                     [--grid_size GRID_SIZE]

optional arguments:
  -h, --help            show this help message and exit
  --ndinos NDINOS       the number of dinosaurs to simulate.
  --ntrees NTREES       the number of avocado trees to simulate.
  --grid_size GRID_SIZE
                        the size of the square grid, in units (one dimension).
```

If you want a more interesting simulation, try adding a lot more dinosaurs
or trees!

```bash
dinolemma gui --ndinos 100 --ntrees 30
```

What you'll likely see given those ratios are that the dinosaurs (purple) eat one another 
(or starve) and then the trees (green) grow to take up the game board.

### Python

You can run a simulation from within Python, either using the defaults:

```
from dinolemma.game import DinosaurDilemma                              

simulation = DinosaurDilemma()                                          
Today is day 13 in the summer season.
There are 1 dinosaurs, and 14 avocado trees.
The temperate is 59°F, humidity 0.43
```

or by setting any of the variables (number of dinosaurs or trees, size of grid, etc.)

## Development

The way that I'm thinking about this project is in stages. 

### Stage 1: Stateful

#### 1. Environment

The first thing to design is the environment, meaning a stateful base that has a set of variables (e.g., temperature, humidity) that will vary
on some regular increment and then influence the entities that live in it downstream. For example, a base environment might 
be defined by a season and day that leads to a particular temperature that has downstream influences on the organisms that live
in it. If my environment has a function to cycle through a unit (e.g., a day) then I can update it's state, and
then update the entities in it depending on the new state.

#### 2. Entities

Once the environment is defined, the next level of stateful objects must be defined, the entities that live within
the environment. The entities should first update themselves based on the changed environment, and then interact.
Interaction comes down to each entity changing location on some grid, and if the location is in the vicinity
of another organism, then the interaction occurs. I thought about whether I wanted all entities to move (and then 
interact) versus allowing them to interact as they move, and I chose the latter. The reason is because
we would allow for multiple interactions for any given entity in one turn, and that's more interesting.
To be fair, I have to ensure that the order of movement is randomized. And notably, avocado trees cannot
move.

#### 3. Interactions

Every entity must have defined rules for interaction with other entities. When all entities
in the simulation change location, those that are within some vicinity of one another
are allowed to interact. Interaction can further influence the state of the entity,
or even lead to creation or destruction of said entity.

At the end of the design of stage 1, we will have developed essentially a text based, stateful simulation.
We will be able to run it with some set of starting conditions, and then observe the interactions
over a particular number of time steps (days) and some final outcome.

### Stage 2: Graphical

Once the stateful simulation is designed, we should strive to visualize it. This
means (possibly) re-implementation in a browser based language that can render
objects on a canvas or via the dom (d3.js). We would want to be able to run
the same text based simulation, and watch it.

### Stage 3: Live

The stateful approach works for early design, but what we would really want is essentially
a bunch of entities that are co-existing in an environment, and then reacting to one another.
I think we could try to emulate this with something that looks more like a bunch of
objects that can emit and subscribe to one another's events, and then know how to
respond.


## Characters

### Dinosaurs

Dinosaurs are the main character in this world, and we initialize the world
with some number. Specifically, a dinosaur wanders around and has the following
attributes:

 - **hunger**: each dinosaur is hungry, and gets more hungry as the simulation progresses. If the dinosaur enconuters a ripe avocado, he will eat it and the hunger subside. Each dinosaur has a slightly different threshold for deciding to eat.
 - **size**: each dinosaur has a randomly set size. A larger dinosaur is obviously requiring more food than a smaller one, and a larger one is also advantaged to be able to eat a smaller dinosaur, if desperate.
 - **disease**: if a dinosaur is hungry and eats an avocado or another dinosaur with a disease, he can get sick. A sick dinosaur moves less, and thus has a greater chance of dying due to hunger or even being eaten by another dinosaur.
 - **gender**: A dinosaur has a 45% change of being male or female, and a 10% chance of being a hybrid, which can reproduce without a mate. Only mature dinosaurs (greater than or equal to 80% of their full adult size) can reproduce, and with every interaction, there is only some small percentage of it.

The dinosaur has the following actions:

 - **move**: for each turn of the game, the dinosaur moves, and then interacts with whatever he finds in his new spot.
 - **eat**: a dinosaur can choose to eat an avocado, or even another dinosaur, depending on the size and level of hunger.
 - **sleep** a dinosaur can choose to sleep (with some probability) if he is sick to increase the chance of getting better.
 - **reproduce** a dinosaur that encounters another dinosaur (mature of the opposite gender) has some percent change of reproduction.

### Avocados

Avocados are grown on trees that are scattered in the environment. For any given tree, it must be a certain age to produce avocados, and once it's old enough, it can only generate a certain number of avocados over a period of time. This gives us the following attributes:

 - **mature**: a mature tree cannot be eaten by a dinosaur, and can produce avocados. An immature tree can be eaten entirely and removed from the game.
 - **avocados**: once a tree is mature, it holds a certain number of avocados
 - **disease**: any tree can get a disease with a small probability. Getting a disease puts the tree at risk for dying, or getting a dinosaur sick.

## Variables

For each of the scenarios above, there must be probabilities generated within some range (set when the game starts) and then allocated to randomly generated entities, which are also randomly placed on a game board of some size.

### Dinosaurs

The game starts with a certain number of dinosaurs (number of total dinosaurs), with the following randomly set values (within some ranges):

 - size
 - hunger

The game itself (an instance of DinosaurDilemma) under [dinolemma/game.py](dinolemma/game.py) creates
some number of dinosaurs in the following way:

```python
from dinolemma.dinosaurs import Dinosaurs

dinosaurs = Dinosaurs()

dinosaurs
[14 dinosaurs]

for dino in dinosaurs: 
    print(dino.name) 

persnickety-muffinpodus
loopy-tacopodus
gassy-poodledocus
frigid-nalgasasaurus
hanky-dogdocus
dirty-blackbeanpodus
astute-truffleus
loopy-knifeus
chocolate-noodleisaurus
psycho-chipiraptor
muffled-lizardus
stinky-underoosdocus
rainbow-cattywampusisaurus
buttery-saladiraptor
```

Each is guaranteed to have a unique name, and we check that there are enough
spaces on the game board to support the dinosaurs and trees created. We
can also grab a random dinosaur:

```python
dino = dinosaurs.random()
dino.name
'bricky-eagleraptor'
```

### Avocados
The game also starts with a certain number of avocado saplings.

```python
from dinolemma.avocados import AvocadoTrees

trees = AvocadoTrees()
for tree in trees:
    print(tree.name)

hanky-egg-tree
goodbye-poo-tree
reclusive-sundae-tree
muffled-squidward-tree
```

or grab a random tree:

```python
tree = trees.random()
tree
<dinolemma.avocados.AvocadoTree at 0x7f25347e7860>
```
