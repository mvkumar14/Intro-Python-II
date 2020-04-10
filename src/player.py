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

        # Not using this in the rest of code yet. 
        # refactor to put it to use.
        inventory_names = []
        for i in self.inventory:
            inventory_names.append(i.name)
        self.inventory_names = inventory_names

    def add_items(self,new_item):
        self.inventory.append(new_item)
    
    def get_item(self, name):
        self.current_room.list_items()
        picked_up = self.current_room.get_item(name)
        if picked_up:
            self.inventory.append(picked_up)
            picked_up.on_take()

    
    def drop_item(self,name):
        inventory_names = []
        for i in self.inventory:
            inventory_names.append(i.name)
        
        if name in inventory_names:
            inventory_list = []
            for i in self.inventory:
                inventory_list.append(i.name)
            inventory_item_position = inventory_list.index(name)
            inventory_item = self.inventory[inventory_item_position]
            del self.inventory[inventory_item_position]
            inventory_item.on_drop()
        else:
            print(f"You don't have a {name}")
        # Right now this function destroys the item 
        # as it is dropped
        # make it so that the item moves to the room
        # inventory when it is dropped
        
        
    def get_all(self):
        if len(self.current_room.items) > 0:
            picked_up_items = self.current_room.get_all()
            for item in picked_up_items:
                i.on_take()
            self.inventory.extend(picked_up_items)
        else:
            print("There is no 'all' in this room ... :P\n" )

    def take_items(self):
        self.inventory.extend(self.current_room.take_items())
    
    def print_inventory(self):
        print('You have:\n')
        for i in self.inventory:
            print(i)

    def move(self,direction):
        if getattr(self.current_room,f"{direction}_to"):
            new_room = getattr(self.current_room,f"{direction}_to")
            self.current_room = new_room
            print(self.current_room)
        else:
            self.error_no_room()
    
    def error_no_room(self):
        print("There is no room in that direction. Try again!\n")