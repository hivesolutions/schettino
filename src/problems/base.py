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

class Problem(object):
    """
    The base class for describing a problem for
    the schettino system.
    """

    persons = ()
    """ The persons to be allocated to the tasks
    this are the names for the domain ranges """

    persons_count = 0
    """ The number of persons available to be scheduled
    in the current problem """

    bitmap = ()
    """ The base bitmap that controls the scheduling
    of the task in a per time basis """

    rules = ()
    """ The set of rules to be executed on the verify
    method this way it's possible to control what
    kind of verification are done """

    number_days = 0
    """ The number of days in the problem, this value
    is previously calculated for performance reasons """

    number_hours = 0
    """ The number of hours in the problem, this value
    is previously calculated for performance reasons """

    number_items = 0
    """ The number of items available in the bitmap
    for processing """

    solution = None
    """ The reference to the current solution, this should
    be the reference to the solution created by the last
    ran solving """

    def __init__(self):
        self.persons_count = len(self.persons)
        self.number_items = self.number_days * self.number_hours
        self.set_rules()

    def set_rules(self, rules = None):
        rules = rules or self.rules
        
        self._rules = []
        
        for rule in self.rules:
            method = getattr(self, rule)
            self._rules.append(method) 

    def rule_1(self, solution):
        """
        Runs the rules that constrains the execution
        of a task to certain number of hours per day.

        This rule is named - work day time rule.
        """

        for index in xrange(len(solution)):
            if index % self.number_hours == 0: counter = self._list_p()

            hour = solution[index]
            if not hour == -1: counter[hour] += 1

            if (index + 1) % self.number_hours == 0:
                for count in counter:
                    if count == 0 or count in self.hours_day: continue
                    return False

        return True

    def rule_2(self, solution):
        counter = self._list_p()

        for index in xrange(len(solution)):
            if index % self.number_hours == 0: _counter = self._list_p()

            hour = solution[index]
            if not hour == -1: _counter[hour] += 1

            if (index + 1) % self.number_hours == 0:
                index = 0
                for count in _counter:
                    if count > 0: counter[index] += 1
                    index += 1

        for count in counter:
            if count <= self.max_days_week: continue
            return False

        return True

    def verify(self, solution = None):
        # tries to retrieve the appropriate solution
        # (defaulting to the current set solution)
        solution = solution or self.solution

        for rule in self._rules:
            result = rule(solution)
            if result: continue
            return result

        # returns valid, because all the rules have
        # passed successfully
        return True

    def get_structure(self):
        # in case there is no solution it's impossible
        # to "calculate" the problem structure, returns
        # immediately with an invalid value
        if not self.solution: return None

        # starts the initial value for the structure (treated
        # solution value) and for the day and item
        structure = []
        day = []
        item = {}

        for index in range(len(self.solution)):
            if index % self.number_hours == 0:
                item = {}
                day = []
                structure.append(day)

            # retrieve the value (index) from the solution and then
            # uses it to retrieve the appropriate string value using
            # the problem definition for the resolution process
            value = self.solution[index]
            value_s = value == -1 and "&nbsp;" or self._shorten_name(self.persons[value])

            # retrieves the previous index (value) from the previous
            # iteration and compares it with the current value in case
            # the value is the same reuses the item
            value_p = item.get("index", None)
            if value == value_p:
                item["size"] += 1
            else:
                item = {
                    "index" : value,
                    "name" : value_s,
                    "time" : "12:30",
                    "size" : 1
                }
                day.append(item)

        return structure

    def print_s(self, solution = None):
        solution = solution or self.solution
        if not solution: raise RuntimeError("No solution is available in problem")

        for index in xrange(len(solution)):
            if index % self.number_hours == 0: print "day %d ::" % (index / self.number_hours),

            hour = solution[index]
            person = hour > -1 and self.persons[hour] or "undefined"
            print "%s, " % person,

            if (index + 1) % self.number_hours == 0: print ""

    def _shorten_name(self, name):
        parts = name.split(" ")
        parts_length = len(parts)
        if parts_length == 1: return name
        first = parts[0]
        last = parts[-1]

        return first + " " + last[0] + "."

    def _list_p(self):
        """
        Creates a new empty list for the currently defined
        person domain problem.

        This is a utility function to be used to shorten the
        time used to create a list of counters for persons.

        @rtype: List
        @return: The newly created zeroed list of counters
        for the various persons.
        """

        return [0 for _value in range(self.persons_count)]
