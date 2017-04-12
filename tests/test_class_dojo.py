#!/usr/bin/env python
# encoding: utf-8


import unittest
from scripts.class_dojo import Dojo


class TestClassDojo(unittest.TestCase):
    # test1: test if new room is appended to list (well done in the example)
    # test2: reject room addition if name already exists...

    def test_create_room_successfully(self):  # test1: done in example
        room_class_instance = Dojo()
        initial_room_count = len(room_class_instance.all_rooms)
        blue_office = room_class_instance.create_room('Blue', 'office')
        self.assertTrue(blue_office)
        new_room_count = len(room_class_instance.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_reject_existing_room(self):
        pass

    # test1: test if a person is added to the list of people succesfully
    # test2: test if a person is rejected if he already exists
    def test_add_person_successfully(self):
        pass

    def test_reject_existing_person(self):
        pass
