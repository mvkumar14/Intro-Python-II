# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, current_room, name='Hero', inventory=None):
        self.name = name
        self.current_room = current_room
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []
    def add_item(self,new_item):
        self.inventory.append(new_item)

    def move(self,new_room):
        self.current_room = new_room