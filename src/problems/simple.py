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

import base

class SimpleProblem(base.Problem):
    number_days = 7
    number_hours = 13
    max_hours_day = 7
    max_days_week = 6
    rules = (
        "rule_1",
        "rule_2"
    )
    persons = (
        "Ana Palhares",
        "Rita Jerónimo",
        "Ana Isabel",
        "Alexandra Lopes",
        "Albano Madureira"
    )
    timetables = (
        ("morning", "intermediate", "night", "morning_s"),
        ("morning", "intermediate", "night", "morning_s"),
        ("morning", "intermediate", "night", "morning_s"),
        ("morning", "intermediate", "night", "morning_s"),
        ("morning", "intermediate", "night", "morning_s"),
        ("morning", "intermediate", "night", "morning_s"),
        ("morning", "intermediate", "night", "morning_s")
    )
    bitmap = (
        1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1
    )
    timetables_r = {
        "morning" : (
            1, 1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0
        ),
        "intermediate" : (
            0, 0, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0
        ),
        "night" : (
            0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 1, 1,
            0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 1, 1,
            0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 1, 1,
            0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 1, 1,
            0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 1, 1,
            0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 1, 1,
            0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 1, 1
        ),
        "morning_s" : (
            1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0
        )
    }
    persons_r = {
        "Rita Jerónimo" : {
            "timetables" : (
                ("morning_s",),
                ("morning_s",),
                ("morning_s",),
                ("morning_s",),
                ("morning_s",),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night")
            ),
            "bitmap" : (
                1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0
            ),
            "max_hours_day" : 3
        }
    }
