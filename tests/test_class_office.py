import unittest
from scripts.class_room import Room


class TestOffice(unittest.TestCase):
    # test1: test that duplicate rooms are not created.
    # test2: test that new rooms are successfully created.
    # test3: test that rooms can be counted.
    def test_add_existing_room(self):
        self.assertEqual(Room('Office', 'White').add_new_room(
        )[0], 'Room White already exists.', 
        'Should not create duplicate rooms')  # test1

    def test_new_room(self):
        self.assertEqual(Room('Office', 'Amber').add_new_room()[0],
                         'An Office called Amber has been successfully created.',
                         'Should be able to create a new room.')  # test2

    def test_count_rooms(self):
        self.assertEqual(Room('Office', 'Blue').get_all_rooms(), 4,
                         'Should be able to count all the rooms.')  # test3
