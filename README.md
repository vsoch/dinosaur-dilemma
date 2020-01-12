# Dinosaur Dilemma

This is the dinosaur dilemma, my first attempt at a simulation. It will involve
characters, interactions, and variables that control those interactions.
The characters will interact in a basic world and at the end, we will be
interested to know how they turned out (evolved).

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
of another organism, then the interaction occurs.

#### 3. Interactions

Every entity must have defined rules for interaction with other entities. When all entities
in the simulation change location, those that are within some vicinity of one another
are allowed to interact. Interaction can further influence the state of the entity,
or even lead to creation or destruction of said entity.

At the end of the design of stage 1, we will have developed essentially a text based, stateful simulation.
We will be able to run it with some set of starting conditions, and then observe the interactions
over a particular number of time steps (days) and some final outcome.

### Stage 2: Graphical

Once the statful simulation is designed, we should strive to visualize it. This
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

The dinosaur has the following actions:

 - **move**: for each turn of the game, the dinosaur moves, and then interacts with whatever he finds in his new spot.
 - **eat**: a dinosaur can choose to eat an avocado, or even another dinosaur, depending on the size and level of hunger.
 - **sleep** a dinosaur can choose to sleep (with some probability) if he is sick to increase the chance of getting better.

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

The game also starts with a certain number of avocado saplings.

**under development**
