# Dinosaur Dilemma

This is the dinosaur dilemma, my first attempt at a simulation. It will involve
characters, interactions, and variables that control those interactions.
The characters will interact in a basic world and at the end, we will be
interested to know how they turned out (evolved).

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
