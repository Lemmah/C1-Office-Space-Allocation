#!/usr/bin/env python
# encoding: utf-8

'''

This is the master of this game. The control class so to call it.
It calls instances of other classes and
mainly interacts with the docopt user interface.

'''
from class_office import Office
from class_living_space import LivingSpace


class Dojo:
    def __init__(self):
        self.all_rooms = []
        self.office_rooms = []
        self.living_places = []
        self.all_people = []
        self.fellows = []
        self.staff = []
        self.allocated_persons = []
        self.unallocated_persons = []

    def create_room(self, room_name, room_type):
        pass

    def add_person(self, person_name, person_type, wants_accomodation='N'):
        pass

    def check_capacity_full(self, room_name):
        pass

    def allocate_office(self):
        pass

    def allocate_room(self):
        pass

    def reallocate_person(self, person_name, new_room_name):
        pass

    def print_room_members(self, room_name):
        pass
