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

import problems.simple

def solve(problem, value = None, all = False, callback = None):
    solution = []
    problem.solution = _solve(problem, solution, value, all, callback)
    return problem.solution

def _solve(problem, solution, value = None, all = False, callback = None):
    # rule1: so posso trabalhar no maximo 7 horas / dia
    # rule2: so posso trabalhar 6 dias por semana
    # rule3: so pode trabalhar no horario da manha (rita only)
    # estas regras ja sao boas para começar

    # tenho de utilizar um decorator para decorar as
    # varias pessoas (unidade de alocacao) ao trabalho

    # in case the provided value is not set (first execution)
    # must start some values to be able to execute
    if value == None:
        position = 0

    # otherwise it's a "normal" execution and the incremental
    # solution must be created and validated (backtracking)
    else:
        solution = solution + [value]
        result = problem.verify(solution)
        if not result: return None

        position = len(solution)
        if position == problem.number_items:
            callback and callback(problem, solution)
            return solution

    if problem.bitmap[position] == 0:
        result = _solve(problem, solution, -1, all, callback)
        if all: pass
        elif result: return result
    else:
        for index in range(problem.persons_count):
            result = _solve(problem, solution, index, all, callback)
            if all: continue
            if not result: continue
            return result

    return None

#COUNTER = 0

def handler(problem, solution):
    problem.print_s(solution)
    #print solution
    #global COUNTER
    #COUNTER += 1
    #print COUNTER

def run():
    problem = problems.simple.SimpleProblem()
    solve(problem, all = True, callback = handler)

if __name__ == "__main__":
    run()
