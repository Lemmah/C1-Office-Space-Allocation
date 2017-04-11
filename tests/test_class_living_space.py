#!/usr/bin/env python
# encoding: utf-8

import unittest
from scripts.class_living_space import *

'''

Class living space inherits the class room

'''


class TestLivingSpace(unittest.TestCase):
    # test1: test that class living space can access the add_new_room method
    # test2: test that class living space can get_room_capacity
    # test3: test that class living space can count all rooms
    def test_add_existing_room(self):
        self.assertEqual(Room('Office', 'White').add_new_room(
        ), 'Room White already exists.', 'Class should inherit Room.')  # test1

    def test_new_room(self):
        self.assertEqual(Room('Office', 'Amber').add_new_room(),
                         'An Office called Amber has been successfully created.',
                         'Class should behave like room.') # test2
