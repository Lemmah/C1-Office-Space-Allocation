#!/usr/bin/env python
# encoding: utf-8

'''

This is the master of this game. The control class so to call it.
It calls instances of other classes and
mainly interacts with the docopt user interface.

'''
import random
from scripts.class_room import Room
from scripts.class_office import Office
from scripts.class_living_space import LivingSpace
from scripts.class_person import Person
from scripts.class_fellow import Fellow



class Dojo:
    def __init__(self):
        self.allocations = {}
        self.all_rooms = []
        self.office_rooms = []
        self.living_places = []
        self.unfilled_rooms = []
        self.all_people = []
        self.fellows = []
        self.staff = []
        self.allocated_persons = []
        self.unallocated_persons = []
        self.office_members = {}
        self.room_members = {}


    def room_allocations(self):
        fellow = Fellow('James', 'Lemayian', 'Fellow',
                        'Blue').allocate_living_space()
        # Appending values to the dictionary
        self.allocations['{}'.format(fellow[2])] = fellow[1]
        return self.allocations

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
                self.living_places.append(room_name)
                self.all_rooms.append(room_name)
                return 'A livingspace called {} has been successfully created.'.format(room_instance[1])
        else:
            return 'The room {} already exists.'.format(room_name)

    def add_person(
            self, first_name,
            last_name, person_type, wants_accomodation='N'):
        person_name = Person(first_name, last_name).full_name()
        if person_name not in self.all_people:
            self.all_people.append(person_name)
            if person_type.lower() == 'staff':
                self.staff.append(person_name)
                if len(self.office_rooms) > 0:
                    allocated_rooms = self.office_members
                    # Allocating staff office
                    room_occurences = [
                        rooms for rooms in allocated_rooms.values()]
                    room_type = 'office'
                    for room in room_occurences:
                        room_capacity = Room(
                            room, room_type).room_details()[2]
                        if room_capacity > room_occurences.count(room):
                            if room not in self.unfilled_rooms:
                                self.unfilled_rooms.append(room)
                    if len(self.unfilled_rooms) > 0:
                        selected_room = random.choice(self.unfilled_rooms)
                        self.office_members[person_name] = selected_room
                        return 'Staff {} has been successfullly added.'.format(person_name), '{} has been allocated the office {}.'.format(
                            first_name, selected_room)
                    else:
                        return 'Staff {} has been successfullly added.'.format(person_name), 'Could not allocate. All the rooms are currently full.'
                else:
                    return 'Staff {} has been successfullly added.'.format(person_name), 'You cannot allocate rooms before you create them.'

            else:
                self.fellows.append(person_name)
                self.all_people.append(person_name)
                if wants_accomodation.upper() == 'Y':
                    if len(self.office_rooms) > 0:
                        allocated_rooms = self.office_members
                        # Allocating fellows office
                        room_occurences = [
                            rooms for rooms in allocated_rooms.values()]
                        room_type = 'office'
                        for room in room_occurences:
                            room_capacity = Room(
                                room, room_type).room_details()[2]
                            if room_capacity > room_occurences.count(room):
                                if room not in self.unfilled_rooms:
                                    self.unfilled_rooms.append(room)
                        if len(self.unfilled_rooms) > 0:
                            selected_room = random.choice(self.unfilled_rooms)
                            self.office_members[person_name] = selected_room
                            office_status = '{} has been allocated the office {}.'.format(first_name, selected_room)
                        else:
                            roffice_status = 'Could not allocate office. All the rooms are currently full.'
                    else:
                        office_status = 'You cannot allocate office before you create one.'
                    if len(self.living_places) > 0:
                        allocated_rooms = self.room_members
                        # Word count logic and list comprehensions
                        room_occurences = [
                            rooms for rooms in allocated_rooms.values()]
                        room_type = 'livingspace'
                        for room in room_occurences:
                            room_capacity = Room(
                                room, room_type).room_details()[2]
                            if room_capacity > room_occurences.count(room):
                                if room not in self.unfilled_rooms:
                                    self.unfilled_rooms.append(room)
                        if len(self.unfilled_rooms) > 0:
                            selected_room = random.choice(self.unfilled_rooms)
                            self.room_members[person_name] = selected_room
                            return 'Fellow {} has been successfullly added.'.format(person_name), office_status, '{} has been allocated the livingspace {}.'.format(first_name, selected_room)
                        else:
                            return 'Fellow {} has been successfullly added.'.format(person_name), office_status, 'Could not allocate livingspace. All the rooms are currently full.'
                    else:
                        return 'Fellow {} has been successfullly added.'.format(person_name), office_status, 'You cannot allocate livingspace before you create one.'
                else:
                    if len(self.office_rooms) > 0:
                        allocated_rooms = self.office_members
                        # Allocating fellows office
                        room_occurences = [
                            rooms for rooms in allocated_rooms.values()]
                        room_type = 'office'
                        for room in room_occurences:
                            room_capacity = Room(
                                room, room_type).room_details()[2]
                            if room_capacity > room_occurences.count(room):
                                if room not in self.unfilled_rooms:
                                    self.unfilled_rooms.append(room)
                        if len(self.unfilled_rooms) > 0:
                            selected_room = random.choice(self.unfilled_rooms)
                            self.office_members[person_name] = selected_room
                            return 'Fellow {} has been successfullly added.'.format(person_name), '{} has been allocated the office {}.'.format(
                                first_name, selected_room)
                        else:
                            return 'Fellow {} has been successfullly added.'.format(person_name), 'Could not allocate office. All the rooms are currently full.'
                    else:
                        return 'Fellow {} has been successfullly added.'.format(person_name), 'You cannot allocate office before you create one.'
        else:
            return '{} is already part of the Andela family.'.format(person_name), 0

    def check_capacity_full(self, room_name):
        pass

    def office_occupants(self, room_name):
        pass

    def living_room_occupants(self, room_name):
        pass

    def reallocate_person(self, person_name, new_room_name):
        pass

    def room_occupants(self, room_name):
        pass
