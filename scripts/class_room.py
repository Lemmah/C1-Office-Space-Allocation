from scripts.class_dojo import *


class Room(Dojo):
    def __init__(self, room_type, room_name):
        self.room_type = room_type
        self.room_name = room_name
        self.room_capacity = None
        self.all_rooms = ['White', 'Blue', 'Violet', 'Gray']

    def get_room_capacity(self):
        if self.room_type.upper() != 'OFFICE':
            self.room_capacity = 4
        else:
            self.room_capacity = 6
        return self.room_capacity

    def add_new_room(self):
        if self.room_name not in self.all_rooms:
            self.all_rooms.append(self.room_name)
            if self.room_type.upper() != 'OFFICE':
                return 'A {} called {} has been successfully created.'.format(
                    self.room_type, self.room_name), self.all_rooms
            else:
                return 'An {} called {} has been successfully created.'.format(
                    self.room_type, self.room_name), self.all_rooms
        else:
            return 'Room {} already exists.'.format(self.room_name), 0

    def get_all_rooms(self):
        self.room_count = len(self.all_rooms)
        return self.room_count


# Confirming outputs after tests
# print(Room('Office', 'White').add_new_room())
# print(Room('Office', 'Amber').add_new_room()[0])
# print(Room('Office', 'Blue').get_all_rooms())
