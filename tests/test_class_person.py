#!/usr/bin/env python
# encoding: utf-8

import unittest
from scripts.class_person import *


class TestClassPerson(unittest.TestCase):
    # test1: check whether the default value of a person's room status is
    # unallocated.
    # test2: check that class person returns person's name,
    # room_allocation_status

    def test_room_allocation_status(self):
        self.assertTrue(ClassPerson('James').room_allocation_status ==
                        False, msg='Person should by default have no room.')  # test1
        self.assertEqual(print(ClassPerson('James')), 'James, False',
                         msg='Return value of Person Class should be name, room_allocation_status')  # test2
