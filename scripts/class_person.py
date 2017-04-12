import random
from scripts.class_dojo import Dojo
'''

This is the Person class, parent class to the Fellow and Staff class.
It holds all the attributes common to Fellows and staff such as:
both have to have office_space, name and are only either fellow or staff

'''


class Person:
    def __init__(
            self, person_type=None, first_name=None,
            last_name=None, office_space=None):

        self.person_type = person_type
        self.first_name = first_name
        self.last_name = last_name
        self.office_space = office_space
        self.available_offices = Dojo.available_offices
    def full_name(self):
        if self.first_name is not None:
            if self.last_name is None:
                return '{}'.format(self.first_name)
            else:
                return '{} {}'.format(self.first_name, self.last_name)

    # def allocated_office(self):
    #     if self.office_space is None:
    #         return '{} has been allocated the office {}.'.format(
    #             self.first_name,
    #             random.choice(self.available_offices))
    #     else:
    #         return '{} has been allocated the office {}.'.format(
    #             self.first_name,
    #             self.office_space)
