#!/usr/bin/env python
# encoding: utf-8

from scripts.class_person import Person

'''

This fellow class inherits from Person.
Simple, it only enables fellows get living spaces
since staff should not have living spaces.

'''


class Fellow(Person):
    def __init__(
            self, first_name,
            second_name, person_type):

        super().__init__(first_name, second_name, person_type)
        self.first_name = first_name
        self.second_name = second_name
        self.person_type = person_type

    def fellow_details(self):
        self.full_name = self.full_name()
        return self.full_name
