#!/usr/bin/env python
# encoding: utf-8


import unittest
from scripts.class_dojo import Dojo


class TestClassDojo(unittest.TestCase):
    def __init__(self):
        '''
        testing create_room functionality
        '''
        # test1: test if new room is appended to list (well done in the example)
        # test2: reject room addition if name already exists...
        self.room_class_instance = Dojo()

    def test_create_room_successfully(self):  # test1: done in example
        initial_room_count = len(self.room_class_instance.all_rooms)
        blue_office = self.room_class_instance.create_room('Blue', 'office')
        self.assertTrue(blue_office)
        new_room_count = len(self.room_class_instance.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    # test2: reject recreation of existing rooms
    def test_reject_existing_room(self):
        blue_room = self.room_class_instance.create_room('Blue', 'Office')
        blue_room
        self.assertEqual(blue_room,
                         'The room Blue already exists.',
                         'The room should be appended to the list.')
    '''
    testing add_person functionality
    '''
    # test1: test if a person is added to the list of people succesfully
    # test2: test if a person is rejected if he already exists

    def test_add_person_successfully(self):  # test1
        fellow = self.room_class_instance.add_person(
            'James', 'Lemayian', 'Fellow' 'Y')
        self.assertTrue(fellow)

    def test_reject_existing_person(self):  # test2
        fellow = self.room_class_instance.add_person(
            'James', 'Lemayian', 'Fellow', 'Y')
        fellow
        self.assertEqual(fellow, 'Person with the same name already exits.')

    '''
    testing office allocation functionality
    '''
    # test1: test that a person is allocated to an office
    # test2: test that a person is not allocated to two offices

    def test_office_allocation(self):
        office_occupants_dict = self.room_class_instance.office_members
        office = self.room_class_instance.add_person(
            'James', 'Lemayian', 'Fellow', 'Y')
        office
        self.assertTrue('James Lemayian' in office_occupants_dict.values())

    def test_single_office_allocation(self):
        office_allocation = self.room_class_instance.add_person(
            'John', 'Doe', 'Fellow', 'Y').count_allocation
        self.assertEqual(office_allocation, 1,
                         'Should be allocated one office only.')

    '''
    testing room allcation functionality
    '''
    # test1: test that a staff is not allocated a room
    # test2: test that the fellow is not allocated two rooms

    def test_livingroom_allocation(self):
        room_occupants_dict = self.room_class_instance.room_members
        room = self.room_class_instance.add_person(
            'James', 'Lemayian', 'Fellow', 'Y')
        room
        self.assertTrue('James Lemayian' in room_occupants_dict.values())

    def test_single_room_allocation(self):
        room_allocation = self.room_class_instance.add_person(
            'John', 'Doe', 'Fellow', 'Y').count_allocation
        self.assertEqual(room_allocation, 1,
                         'Should be allocated one office only.')
