#!/usr/bin/env python
# encoding: utf-8

'''

This is the Person class, parent class to the Fellow and Staff class.
It holds all the attributes common to Fellows and staff such as:
both have to have office_space, name and are only either fellow or staff

'''


class Person:
    def __init__(
            self, first_name=None,
            last_name=None, office_space=None):

        self.first_name = first_name
        self.last_name = last_name
        self.office_space = office_space

    # Giving back full name even when one name is specified, I just want to
    # inherit it.
    def full_name(self):
        if self.first_name is not None:
            if self.last_name is None:
                return '{}'.format(self.first_name)
            else:
                return '{} {}'.format(self.first_name, self.last_name)
