"""

This is the parent class for subclasses: LivingSpace and Office
The subclasses will inherit the available methods

"""
class Room:
    def __init__(self, room_type, room_name, occupants=0, room_capacity=0):
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
