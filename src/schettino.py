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

import problems.complex as problem

def list_p():
    """
    Creates a new empty list for the currently defined
    person domain problem.

    This is a utility function to be used to shorten the
    time used to create a list of counters for persons.

    @rtype: List
    @return: The newly created zeroed list of counters
    for the various persons.
    """

    return [0 for _value in range(problem.PERSONS_COUNT)]

def rule_1(solution):
    """
    Runs the rules that constrains the execution
    of a task to certain number of hours per day.

    This rule is named - work day time rule.
    """

    for index in xrange(len(solution)):
        if index % problem.N_HOURS == 0: counter = list_p()

        hour = solution[index]
        if not hour == -1: counter[hour] += 1

        if (index + 1) % problem.N_HOURS == 0:
            for count in counter:
                if count == 0 or count in problem.HOURS_DAY: continue
                return False

    return True

def rule_2(solution):
    counter = list_p()

    for index in xrange(len(solution)):
        if index % problem.N_HOURS == 0: _counter = list_p()

        hour = solution[index]
        if not hour == -1: _counter[hour] += 1

        if (index + 1) % problem.N_HOURS == 0:
            index = 0
            for count in _counter:
                if count > 0: counter[index] += 1
                index += 1

    for count in counter:
        if count <= problem.MAX_DAYS_WEEK: continue
        return False

    return True

def rules(solution):
    _rules = (rule_1, rule_2)

    for rule in _rules:
        result = rule(solution)
        if result: continue
        return result

    return True

def solve(solution, value = None, i = 0, all = False, callback = None):
    # tenho de alocar para x dias do mes
    # vou primeiro alocar para uma semana

    # rule1: so posso trabalhar no maximo 7 horas / dia
    # rule2: so posso trabalhar 6 dias por semana
    # rule3: so pode trabalhar no horario da manha (rita only)
    # estas regras ja sao boas para começar

    # tenho de utilizar um decorator para decorar as
    # varias pessoas (unidade de alocacao) ao trabalho

    if not value == None:
        solution = solution + [value]
        result = rules(solution)
        if not result: return None

        i += 1
        if i == problem.N_ITEMS:
            callback and callback(solution)
            return solution

    if problem.BITMAP[i] == 0:
        result = solve(solution, -1, i, all, callback)
        if all: pass
        elif result: return result
    else:
        for index in range(problem.PERSONS_COUNT):
            result = solve(solution, index, i, all, callback)
            if all: continue
            if not result: continue
            return result

    return None

COUNTER = 0

def tobias(solution):
    print_solution(solution)
    #print solution
    #global COUNTER
    #COUNTER += 1
    #print COUNTER

def run():
    solution = []
    solve(solution, all = True, callback = tobias)

def print_solution(solution):

    for index in xrange(len(solution)):
        if index % problem.N_HOURS == 0: print ":: DAY %d ::" % (index / problem.N_HOURS)

        hour = solution[index]
        person = hour > -1 and problem.PERSONS[hour] or "Unset"
        print "%s, " % person,

        if (index + 1) % problem.N_HOURS == 0: print ""

    print "====================================="

if __name__ == "__main__":
    run()
