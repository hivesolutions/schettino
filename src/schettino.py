#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Schettino System
# Copyright (C) 2008-2012 Hive Solutions Lda.
#
# This file is part of Hive Schettino System.
#
# Hive Schettino System is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Schettino System is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Schettino System. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2012 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

PERSONS = ["Ana", "Sofia", "Alexandra"]
""" The persons to be allocated to the tasks
this are the names for the domain ranges """

import constraint

def run():
    problem = constraint.Problem()

    domain = range(len(PERSONS))

    problem.addVariable("D1H1", domain)
    problem.addVariable("D1H2", domain)

    # retrieves a solution for the problem
    # and prints it a beautiful manner
    solutions = problem.getSolutions()
    for solution in solutions:
        print_solution(solution)
        print ""

def print_solution(solution):
    keys = solution.keys()
    keys.sort()

    for key in keys:
        value = solution[key]
        person = PERSONS[value]
        print "KEY := %s" % person

if __name__ == "__main__":
    run()
