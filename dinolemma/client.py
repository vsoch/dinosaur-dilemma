#!/usr/bin/env python

"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from dinolemma.game import DinosaurDilemma
import dinolemma
import argparse
import sys
import os


def get_parser():
    parser = argparse.ArgumentParser(description="Dinosaur Dilemma simulator")
    parser.add_argument(
        "--version",
        dest="version",
        help="suppress additional output.",
        default=False,
        action="store_true",
    )

    description = "actions for Dinosaur Dilemma simulator"
    subparsers = parser.add_subparsers(
        help="dinolemma actions",
        title="actions",
        description=description,
        dest="command",
    )

    run = subparsers.add_parser("run", help="run a Dinosaur Dilemma simulation")
    gui = subparsers.add_parser(
        "gui", help="run a Dinosaur Dilemma simulation in the graphical interface"
    )

    for command in [run, gui]:
        command.add_argument(
            "--ndinos",
            dest="ndinos",
            help="the number of dinosaurs to simulate.",
            type=int,
            default=None,
        )

        command.add_argument(
            "--ntrees",
            dest="ntrees",
            help="the number of avocado trees to simulate.",
            type=int,
            default=None,
        )

        command.add_argument(
            "--grid_size",
            dest="grid_size",
            help="the size of the square grid, in units (one dimension).",
            type=int,
            default=25,
        )

    return parser


def main():
    """main is the entrypoint to the juliart client.
    """

    parser = get_parser()

    # Will exit with subcommand help if doesn't parse
    args, extra = parser.parse_known_args()

    # Show the version and exit
    if args.version:
        print(dinolemma.__version__)
        sys.exit(0)

    # Run text based simulation
    if args.command == "run":
        simulation = DinosaurDilemma(
            grid_size=args.grid_size, number_trees=args.ntrees, number_dinos=args.ndinos
        )
        simulation.run()

    # Run graphical simulation
    elif args.command == "gui":
        from dinolemma.gui import run_game

        run_game(
            grid_dim=args.grid_size, number_trees=args.ntrees, number_dinos=args.ndinos
        )

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
