#!/usr/bin/env python
# encoding: utf-8

import unittest
from scripts.class_person import *


class TestClassPerson(unittest.TestCase):
    # test1: check whether the default value of a person's room status is
    # unallocated.
    # test2: should be able to get full names when both names are provided
    # test3: add new person returns the correct statement

    def test_room_allocation_status(self):
        self.assertTrue(Person('James').office_space is
                        None, 'Person should by default have no room.')  # test1

    def test_full_name_generation(self):
        self.assertEqual(Person('Fellow', 'James', 'Lemayian').full_name(),
                         'James Lemayian',
                         'The full name should be a conc of first and second name!')  # test2

    def test_add_new_person(self):
        self.assertEqual(Person('Fellow', 'Joshua', 'Ondieki').new_person(
        ), 'Fellow Joshua Ondieki has been successfully added.')  # test3
