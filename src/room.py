# Implement a class to hold room information. This should have name and
# description attributes.


# Maybe refactor code so that the internal state representation of a
# list of items can be more easily accessed. This could build out
# into an inventory object which is subclassed by both the room object, and the 
# player object.

# it would be a "has-a" relationship.

class Room():
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None 
        if items == None:
            self.items = []
        else: 
            self.items = items

    def add_item(self,item):
        self.items.append(item)
    
    def add_items(self,items):
        for i in items:
            self.items.append(i)

    def get_items(self):
        room_items = self.items
        self.items=[]
        return room_items
    
    def get_item(self,name):
        item_names = []
        for i in self.items:
            item_names.append(i.name)
        if name in item_names:
            # The position of the item in the main object list
            list_position = item_names.index(name)
            # Popping the object from the list and returning it 
            return self.items.pop(list_position)
        else:
            print(f"Hmm strange... There is no {name} here\n")
            pass
    
    def get_all(self):
        out_list = self.items
        self.items = []
        return out_list
    
    def list_items(self):
        if len(self.items)>0:
            items_list = []
            for i in self.items:
                items_list.append(i.name)
            str_rep = (',').join(items_list)
            print(f'Here are the items in this room: {str_rep}\n')
        else:
            print('There are no items in this room\n')   
        pass         

    def __str__(self):
        str_rep = f'You are now in the {self.name} room.\n\n{self.description}\n'
        return str_rep
    