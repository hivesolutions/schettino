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

PERSONS = ["Ana", "Tobias", "Matias", "Rabeton"]
""" The persons to be allocated to the tasks
this are the names for the domain ranges """

PERSONS_COUNT = len(PERSONS)
""" The number of persons available to be scheduled
in the current problem """

BITMAP = (
    (1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
)
""" The base bitmap that controls the scheduling
of the task in a per time basis """


#BITMAP = (
#    (1, 0),
#    (1, 1),
#    (0, 0)
#)


N_DAYS = len(BITMAP)
""" The number of days in the problem, this value
is previously calculated for performance reasons """

N_HOURS = len(BITMAP[0])
""" The number of hours in the problem, this value
is previously calculated for performance reasons """

def rule_1(solution):
    """
    Runs the rules that constrains the execution
    of a task to certain number of hours per week.

    This rule is named - work week time rule.
    """

    # tenho de poder fazer cortes !!!!
    # por exemplo com cache de count por dias

    for day in solution:
        counter = [0 for _value in range(PERSONS_COUNT)]

        for hour in day:
            if hour == -1: continue
            counter[hour] += 1

        for count in counter:
            if count <= 7: continue #@TODO: HARDCODED MUST BE CONFIGURABLE !!!
            return False

    return True

def rule_2(solution):
    # CADA PESSOA SO PODE TRABALHAR 6 dias por semana

    counter = [0 for _value in range(PERSONS_COUNT)]

    for day in solution:
        _counter = [0 for _value in range(PERSONS_COUNT)]

        for hour in day:
            if hour == -1: continue
            _counter[hour] += 1

        _index = 0

        for count in _counter:
            if count > 0: counter[_index] += 1
            _index += 1

    for count in counter:
        if count > 4: return False

    return True

def rules(solution):
    _rules = (rule_1, rule_2)

    for rule in _rules:
        result = rule(solution)
        if result: continue
        return result

    return True

def solve(solution, value = None, i = 0, j = 0, all = False, callback = None):
    # tenho de alocar para x dias do mes
    # vou primeiro alocar para uma semana

    # rule1: so posso trabalhar no maximo 7 horas / dia
    # rule2: so posso trabalhar 6 dias por semana
    # rule3: so pode trabalhar no horario da manha (rita only)
    # estas regras ja sao boas para começar

    # tenho de utilizar um decorator para decorar as
    # varias pessoas (unidade de alocacao) ao trabalho

    if not value == None:
        solution[i][j] = value
        result = rules(solution)
        if not result: return False

        j += 1

        if j == N_HOURS: i += 1; j = 0
        if i == N_DAYS: callback and callback(solution); return True

    if BITMAP[i][j] == 0:
        result = solve(solution, -1, i, j, all, callback)
        if all: pass
        elif result: return result
    else:
        for index in range(PERSONS_COUNT):
            result = solve(solution, index, i, j, all, callback)
            if all: continue
            if not result: continue
            return result

    return False

def tobias(solution):
    print_solution(solution)

def run():
    solution = [[-1 for _value in xrange(N_HOURS)] for _value in xrange(N_DAYS)]
    solve(solution, all = True, callback = tobias)

def print_solution(solution):

    index = 0
    for day in solution:

        print ":: DAY %d ::" % index

        for hour in day:
            person = hour > -1 and PERSONS[hour] or "Unset"
            print "%s, " % person,

        print "\n"

        index += 1

if __name__ == "__main__":
    run()
