#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Schettino System
# Copyright (c) 2008-2020 Hive Solutions Lda.
#
# This file is part of Hive Schettino System.
#
# Hive Schettino System is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Schettino System is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Schettino System. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2020 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import base

class SimpleProblem(base.Problem):
    number_days = 7
    number_hours = 13
    number_days_off = 1
    max_hours_day = 7
    max_days_week = 6
    rules = ()
    days_off = (2, 3, 4)
    persons = (
        ("Rita Jerónimo", 1),
        ("Maryna Lenok", 1),
        ("Inês Pereira", 1),
        ("Sara Silva", 1),
        ("Delfina Gomes", 2),
        ("Ana Palhares", 3),
        ("Ana Isabel", 3),
        ("Alexandra Lopes", 3),
        ("Albano Madureira", 3),
        ("Luana Pagunge", 3),
        ("Fátima Felgueiras", 3),
        ("Pedro Flores", 3)
    )
    timetables = (
        ("morning_s", "intermediate", "night"),
        ("morning_s", "intermediate", "night"),
        ("morning_s", "intermediate", "night"),
        ("morning_s", "intermediate", "night"),
        ("morning_s", "intermediate", "night"),
        ("morning", "intermediate", "night"),
        ("morning", "intermediate", "night")
    )
    bitmap = (
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0
    )
    timetables_r = {
        "morning" : (
            2, 1, 1, 3, 1, 1, 1, 0, 0, 0, 0, 0, 0,
            2, 1, 1, 3, 1, 1, 1, 0, 0, 0, 0, 0, 0,
            2, 1, 1, 3, 1, 1, 1, 0, 0, 0, 0, 0, 0,
            2, 1, 1, 3, 1, 1, 1, 0, 0, 0, 0, 0, 0,
            2, 1, 1, 3, 1, 1, 1, 0, 0, 0, 0, 0, 0,
            2, 1, 1, 3, 1, 1, 1, 0, 0, 0, 0, 0, 0,
            2, 1, 1, 3, 1, 1, 1, 0, 0, 0, 0, 0, 0
        ),
        "intermediate" : (
            0, 0, 2, 1, 1, 1, 3, 1, 0, 0, 0, 0, 0,
            0, 0, 2, 1, 1, 1, 3, 1, 0, 0, 0, 0, 0,
            0, 0, 2, 1, 1, 1, 3, 1, 0, 0, 0, 0, 0,
            0, 0, 2, 1, 1, 1, 3, 1, 0, 0, 0, 0, 0,
            0, 0, 2, 1, 1, 1, 3, 1, 0, 0, 0, 0, 0,
            0, 0, 2, 1, 1, 1, 3, 1, 0, 0, 0, 0, 0,
            0, 0, 2, 1, 1, 1, 3, 1, 0, 0, 0, 0, 0
        ),
        "night" : (
            0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 3, 1, 0,
            0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 3, 1, 0,
            0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 3, 1, 0,
            0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 3, 1, 0,
            0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 3, 1, 0,
            0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 3, 1, 0,
            0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 3, 1, 0
        ),
        "morning_s" : (
            2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
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
                1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
            ),
            "max_hours_day" : 10,
            "number_days_off" : 0
        },
        "Maryna Lenok" : {
            "timetables" : (
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night")
            )
        },
        "Inês Pereira" : {
            "timetables" : (
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night")
            )
        },
        "Sara Silva" : {
            "timetables" : (
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night")
            )
        },
        "Delfina Gomes" : {
            "timetables" : (
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night")
            )
        },
        "Ana Palhares" : {
            "timetables" : (
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night")
            )
        },
        "Ana Isabel" : {
            "timetables" : (
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night")
            )
        },
        "Alexandra Lopes" : {
            "timetables" : (
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night")
            )
        },
        "Albano Madureira" : {
            "timetables" : (
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night")
            )
        },
        "Luana Pagunge" : {
            "timetables" : (
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night")
            )
        },
        "Fátima Felgueiras" : {
            "timetables" : (
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night")
            )
        },
        "Pedro Flores" : {
            "timetables" : (
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night"),
                ("morning", "intermediate", "night")
            )
        }
    }
