#!/usr/bin/env python
# encoding: utf-8


from scripts.class_room import Room

'''

This class inherits from the room.

'''

class LivingSpace(Room):
    def __init__(self, room_type, room_name):
        super().__init__(room_type, room_name)
        self.room_name = room_name
        self.room_type = room_type
