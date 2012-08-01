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

import copy

class Solution(list):
    """
    The base class for the solution of a problem,
    note that it inherits from the base list type
    because all the solution are expected to be
    expressed as a list.
    """

    meta = {}
    """ The meta information map that contains information
    of calculus for the heuristics to be used in the solving """

    def __init__(self):
        self.meta = {}

    def try_extend(self, value):
        _clone = copy.copy(self)
        _clone.append(value)
        _clone.meta = self.meta
        return _clone

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

    persons_r = {}
    """ The map containing the series of "extra" rules
    to be applied to a certain variable index (person) """

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

    instrumentation = {}
    """ The map containing the various debug values for
    instrumentation of the result, this values are of crucial
    importance in the debugging stage """

    delta = 0
    """ The time in milliseconds that took for the last soling
    to execute (useful for benchmark) """

    def __init__(self):
        self.persons_count = len(self.persons)
        self.number_items = self.number_days * self.number_hours
        self.instrumentation = {}
        self.set_rules()

    def set_rules(self, rules = None):
        rules = rules or self.rules

        self._rules = []

        for rule in self.rules:
            method = getattr(self, rule)
            self._rules.append(method)

    def get_ordered(self, solution = None):
        # tries to retrieve the appropriate solution
        # (defaulting to the current set solution)
        solution = self._get_solution(solution)

        position = len(solution)

        current = solution.meta.get("current", 0)
        _range = solution.meta.get("range", 0)
        day_set = solution.meta.get("day_set", range(self.persons_count))
        week = solution.meta.get("week", self._list_p())

        ordered = day_set

        removal = []
        for index in day_set:
            bitmap = self.get_bitmap(index)
            if bitmap[position]: continue
            removal.append(index)

        # in case the removal list is not empty there are
        # items to be removed so the ordered list must be
        # clones and the removal items removed
        if removal:
            ordered = copy.copy(ordered)
            for index in removal: ordered.remove(index)

        return ordered

    def rule_1(self, solution):
        """
        Runs the rules that constrains the execution
        of a task to certain number of hours per day.

        This rule is named - work day time rule.
        """

        for index in xrange(len(solution)):
            if index % self.number_hours == 0: counter = self._list_p()

            item = solution[index]
            if not item == -1: counter[item] += 1

            if (index + 1) % self.number_hours == 0:
                for count in counter:
                    if count == 0 or count <= self.get_max_hours_day(item): continue
                    self._add_failure(self.rule_1.__name__)

                    return False

        return True

    def rule_2(self, solution):
        counter = self._list_p()

        for index in xrange(len(solution)):
            if index % self.number_hours == 0: _counter = self._list_p()

            item = solution[index]
            if not item == -1: _counter[item] += 1

            if (index + 1) % self.number_hours == 0:
                index = 0
                for count in _counter:
                    if count > 0: counter[index] += 1
                    index += 1

        for count in counter:
            if count <= self.max_days_week: continue
            self._add_failure(self.rule_2.__name__)
            return False

        return True

    def verify(self, solution = None):
        # tries to retrieve the appropriate solution
        # (defaulting to the current set solution)
        solution = self._get_solution(solution)

        for rule in self._rules:
            result = rule(solution)
            if result: continue
            return result

        # returns valid, because all the rules have
        # passed successfully
        return True

    def _week_count(self, week_mask):
        count = 0

        for i in range(7):
            if not week_mask & 1 << i: continue
            count += 1

        return count

    def state(self, solution = None):
        # tries to retrieve the appropriate solution
        # (defaulting to the current set solution)
        solution = self._get_solution(solution)

        day = solution.meta.get("day", 0)
        day_set = solution.meta.get("day_set", range(self.persons_count))
        current = solution.meta.get("current", -1)
        _range = solution.meta.get("range", 0)
        week = solution.meta.get("week", self._list_p())
        week_mask = solution.meta.get("week_mask", self._list_p())

        position = len(solution)
        _day = position / self.number_hours
        if not _day == day:
            day_set = range(self.persons_count)

            removal = []
            for item in day_set:
                week_count = self._week_count(week_mask[item])
                if week_count < self.max_days_week: continue
                removal.append(item)

            for item in removal: day_set.remove(item)

            current = -1
            _range = 0

        # retrieves the current item from the solution
        # and in case it's not valid returns immediately
        # (not going to update the state for invalid values)
        item = solution[-1]
        if item == -1: return

        if not week_mask[item] & 1 << _day:
            week[item] += 1
            week_mask[item] |= 1 << _day

        if item == current: _range += 1
        else: _range = 1

        # sets the current element as the last item from the
        # currently available solution (historic reference)
        current = item

        # in case the maximum range has been reached
        # for the current element it must be removed
        # from the day set (new element must be used)
        if _range == self.get_max_hours_day(current): day_set.remove(current)

        # updates the meta information map with the must up to
        # date values so that they can be used latter for performance
        solution.meta["day"] = _day
        solution.meta["day_set"] = day_set
        solution.meta["current"] = current
        solution.meta["range"] = _range
        solution.meta["week"] = week
        solution.meta["week_mask"] = week_mask

    def get_bitmap(self, index):
        person = self.persons[index]
        rules = self.persons_r.get(person, {})
        bitmap = rules.get("bitmap", None)
        if not bitmap: return self.bitmap

        _bitmap = []

        for index in xrange(self.number_items):
            first = self.bitmap[index]
            second = bitmap[index]
            final = first and second or 0
            _bitmap.append(final)

        return _bitmap

    def get_max_hours_day(self, index):
        person = self.persons[index]
        rules = self.persons_r.get(person, {})
        max_hours_day = rules.get("max_hours_day", None)
        if not max_hours_day: return self.max_hours_day
        return max_hours_day

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
        solution = self._get_solution(solution)
        if not solution: raise RuntimeError("No solution is available in problem")

        for index in xrange(len(solution)):
            if index % self.number_hours == 0: print "day %d ::" % (index / self.number_hours),

            hour = solution[index]
            person = hour > -1 and self.persons[hour] or "undefined"
            print "%s, " % person,

            if (index + 1) % self.number_hours == 0: print ""

    def _add_failure(self, name):
        failures = self.instrumentation.get("failures", {})
        failure = failures.get(name, 0)
        failures[name] = failure + 1
        self.instrumentation["failures"] = failures

    def _get_solution(self, solution):
        return solution == None and self.solution or solution

    def _shorten_name(self, name):
        """
        Shortens the provided name so that the first name
        is shown in the complete form and the last name is
        provided only with the first letter.

        @type name: String
        @param name: The name to be shortened.
        @rtype: String
        @return: The shortened version of the provided name.
        """

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
