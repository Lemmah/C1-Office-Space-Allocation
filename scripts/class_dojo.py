#!/usr/bin/env python
# encoding: utf-8

'''

This is the master of this game. The control class so to call it.
It calls instances of other classes and
mainly interacts with the docopt user interface.

'''
from scripts.class_office import Office
from scripts.class_living_space import LivingSpace
from scripts.class_room import Room


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
        if room_name not in self.all_rooms:
            if room_type.lower() == 'office':
                self.all_rooms.append(room_name)
                self.office_rooms.append(room_name)
                room_instance = Office(room_type, room_name).room_details()
                return 'An office called {} has been successfully created.'.format(room_instance[1])
            else:
                room_instance = LivingSpace(
                    room_type, room_name).room_details()
                return 'A livingspace called {} has been successfully created.'.format(room_instance[1])
        else:
            return 'The room {} already exists.'.format(room_name)

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
