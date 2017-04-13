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


class Dojo:
    def __init__(self):
        self.all_rooms = []
        self.office_rooms = []
        self.living_places = []
        self.unfilled_rooms = []
        self.all_people = []
        self.fellows = []
        self.staff = []
        self.allocated_persons = []
        self.unallocated_persons = []
        self.office_members = {}  # testing value
        self.room_members = {}

    def create_room(self, room_name, room_type):
        if room_name not in self.all_rooms:
            if room_type.lower() == 'office':
                self.all_rooms.append(room_name)
                self.living_places.append(room_name)
                self.room_members['None'] = room_name
                room_instance = Office(room_type, room_name).room_details()
                return 'An office called {} has been successfully created.'.format(room_instance[1])
            else:
                self.all_rooms.append(room_name)
                self.office_rooms.append(room_name)
                self.office_members['None'] = room_name
                room_instance = LivingSpace(
                    room_type, room_name).room_details()
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
                        return ['Staff {} has been successfullly added.'.format(person_name), '{} has been allocated the office {}.'.format(
                                                    first_name, selected_room)]
                    else:
                        return ['Staff {} has been successfullly added.'.format(person_name), 'Could not allocate. All the rooms are currently full.']
                else:
                    return ['Staff {} has been successfullly added.'.format(person_name), 'You cannot allocate rooms before you create them.']

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
                            office_status = '{} has been allocated the office {}.'.format(
                                first_name, selected_room)
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
                            return ['Fellow {} has been successfullly added.'.format(person_name), office_status, '{} has been allocated the livingspace {}.'.format(first_name, selected_room)]
                        else:
                            return ['Fellow {} has been successfullly added.'.format(person_name), office_status, 'Could not allocate livingspace. All the rooms are currently full.']
                    else:
                        return ['Fellow {} has been successfullly added.'.format(person_name), office_status, 'You cannot allocate livingspace before you create one.']
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
                            return ['Fellow {} has been successfullly added.'.format(person_name), '{} has been allocated the office {}.'.format(
                                                            first_name, selected_room)]
                        else:
                            return ['Fellow {} has been successfullly added.'.format(person_name), 'Could not allocate office. All the rooms are currently full.']
                    else:
                        return ['Fellow {} has been successfullly added.'.format(person_name), 'You cannot allocate office before you create one.']
        else:
            return ['{} is already part of the Andela family.'.format(person_name), 0, 0]

    def check_capacity_full(self, room_name):
        for room in self.all_rooms:
            ## TODO: implement this class to
            #reduce redundancy of code in adding person.
            if room_name in self.office_rooms:
                room_type = 'office'
                room_occurence = [room_name for room_name in self.office_members]
            elif room_type in self.living_places:
                room_type = 'livingplace'
                room_occurence = [room_name for room_name in self.room_members]
            else:
                pass
            room_capacity = Room(room, room_type).room_details()[2]


    def office_occupants(self, room_name):
        pass

    def living_room_occupants(self, room_name):
        pass

    def print_rooms(self):
        loop_rooms = 1
        for room in self.all_rooms:
            if loop_rooms <= len(self.all_rooms):
                return room

    def reallocate_person(self, person_name, new_room_name):
        pass

    def room_occupants(self, room_name):
        pass
