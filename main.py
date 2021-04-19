#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a demo on class usage and other things...
"""

from models.family.large.large import large_family


def main():
    myfamily = large_family()  # calling our derived class
    myfamily.set_min_members()  # returning from parent class
    myfamily.set_min_age(2)  # setting val on parent class

    print(myfamily.get_type())  # accessing static members through getters
    print(myfamily.get_min_members())  # accessing dynamic data (?)


# calling the actual funct from "main" file
if __name__ == '__main__':
    main()
