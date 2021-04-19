#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# family definition
class family:

    def __init__(self):
        self._type = "family"

    def set_min_members(self, val):
        self._min_members = val

    def get_min_members(self):
        return self._min_members

    def set_min_age(self, val):
        self._min_age = val

    def get_min_age(self):
        return self._min_age

    def get_type(self):  # getters / setters in python
        return self._type
