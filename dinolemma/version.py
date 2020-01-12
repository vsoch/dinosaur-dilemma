"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

__version__ = "0.0.1"
AUTHOR = "Vanessa Sochat"
AUTHOR_EMAIL = "vsochat@stanford.edu"
NAME = "dinolemma"
PACKAGE_URL = "http://www.github.com/vsoch/dinosaur-dilemma"
KEYWORDS = "simulation, dinosaur, avocados"
DESCRIPTION = "Simulate evolution of dinosaurs and avocado trees"
LICENSE = "LICENSE"

################################################################################
# Requirements


INSTALL_REQUIRES = (("numpy", {"min_version": "1.16.2"}),)
TESTS_REQUIRES = (("pytest", {"min_version": "4.6.2"}),)
ANIMATE_REQUIRES = (("imageio", {"min_version": "2.5.0"}),)

INSTALL_REQUIRES_ALL = INSTALL_REQUIRES + ANIMATE_REQUIRES
