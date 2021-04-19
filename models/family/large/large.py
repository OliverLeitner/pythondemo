#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# we expand on family
from models.family.family import family


# and create a new large family class
class large_family(family):
    def __init__(self):
        super().__init__()  # implements parent class
        # print(self._type)  # this should be family
        self._type = "large family"  # now it aint

    def get_type(self):
        return self._type

    def set_min_members(self, val):
        family._min_members = val

    def get_min_members(self):
        if family._min_members <= 2:
            print("too small for large family!")
        return family._min_members
