"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from dinolemma.colors import BLACK, WHITE, GREEN, PURPLE, LIGHT_PURPLE, YELLOW
from dinolemma.game import DinosaurDilemma
import sys

try:
    import pygame
except:
    sys.exit("You must install pygame to use the game interface.")


def text_objects(text, font, color=WHITE):
    """return a text surface and surrounding rectangle
    """
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def show_text(lines, screen, x, y, font_size=30, color=WHITE):
    """Given one or more lines of text, print to screen at center x,y
    """
    if isinstance(lines, str):
        lines = [lines]

    largeText = pygame.font.Font("freesansbold.ttf", font_size)
    for line in lines:
        TextSurf, TextRect = text_objects(line, largeText, color)
        TextRect.center = ((x), (y))
        screen.blit(TextSurf, TextRect)
        y += font_size


def button(
    message,
    screen,
    x_topleft,
    y_topleft,
    width,
    height,
    inactive_color=GREEN,
    active_color=YELLOW,
    font_color=BLACK,
    font_size=20,
):
    """Add a button to the game.
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    clicked = False

    # Interactive - if the mouse is over it, show hover effect
    if (
        x_topleft + width > mouse[0] > x_topleft
        and y_topleft + height > mouse[1] > y_topleft
    ):
        pygame.draw.rect(screen, active_color, (x_topleft, y_topleft, width, height))
        if click[0] == 1:
            clicked = True

    else:
        pygame.draw.rect(screen, inactive_color, (x_topleft, y_topleft, width, height))

    smallText = pygame.font.Font("freesansbold.ttf", font_size)
    textSurf, textRect = text_objects(message, smallText, font_color)
    textRect.center = ((x_topleft + (width / 2)), (y_topleft + (height / 2)))
    screen.blit(textSurf, textRect)
    return clicked


def run_game(grid_size=25, number_trees=None, number_dinos=None, grid_dim=30):
    """run the gui game. Currently, parameters are hard set to ensure that
       dimensions work out okay. This could be modified to be more dynamic

       Parameters
       ==========
       grid_dim: the width and height of a square in the grid
    """
    # Set the WIDTH and HEIGHT of each grid location
    WIDTH = HEIGHT = grid_dim

    # This sets the margin between each cell
    MARGIN = 5
    TEXT_AREA = 200

    # Create the simulation
    simulation = DinosaurDilemma(
        grid_size=grid_size, number_trees=number_trees, number_dinos=number_dinos
    )

    # Initialize pygame
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    SIZE = grid_size * (WIDTH + MARGIN) + MARGIN
    WINDOW_SIZE = [SIZE, SIZE + TEXT_AREA]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Set title of screen
    pygame.display.set_caption("Dinosaur Dilemma")

    # Set the original text on the screen
    summary = simulation.summary(return_summary=True).split("\n")
    show_text(summary, screen, SIZE / 2, SIZE + 10)
    pygame.display.flip()

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    def update_grid(screen, simulation):
        """given a simuation and number of rows/cols, update the game grid
           we define this as a subfunction of run_gui to share the function
           local variables.
        """
        # Set the screen background, display text
        screen.fill(BLACK)

        # Draw the grid
        for row in range(simulation.grid_size):
            for column in range(simulation.grid_size):
                color = WHITE
                if simulation.grid[row][column] is not None:
                    if simulation.grid[row][column].endswith("tree"):
                        color = GREEN
                    else:
                        color = PURPLE
                pygame.draw.rect(
                    screen,
                    color,
                    [
                        (MARGIN + WIDTH) * column + MARGIN,
                        (MARGIN + HEIGHT) * row + MARGIN,
                        WIDTH,
                        HEIGHT,
                    ],
                )

        # Update the message to the viewer
        summary = simulation.summary(return_summary=True).split("\n")
        show_text(summary, screen, SIZE / 2, SIZE + 30)
        show_text(
            ["Click to progress to next day..."],
            screen,
            SIZE / 2,
            SIZE + 150,
            color=LIGHT_PURPLE,
        )

        # Add the bottom
        clicked = button(
            "Reset",
            screen,
            x_topleft=10,
            y_topleft=SIZE + TEXT_AREA - 70,
            width=100,
            height=50,
        )

        # If clicked, restart the simulation
        if clicked:
            simulation = DinosaurDilemma(
                grid_size=grid_size,
                number_trees=number_trees,
                number_dinos=number_dinos,
            )

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        return simulation

    # -------- Main Program Loop -----------
    while not done:

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            # Right now, use any click to progress the game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                simulation.run_day()

            simulation = update_grid(screen, simulation)

    # Don't hang on exit.
    pygame.quit()
