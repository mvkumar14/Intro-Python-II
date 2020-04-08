# Implement a class to hold room information. This should have name and
# description attributes.

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

    def get_items(self):
        room_items = self.items
        self.items=[]
        return room_items
    
    def list_items(self):
        if len(self.items)>0:
            str_rep = (',').join(self.items)
            print(f'Here are the items in this room: {str_rep}\n')
        else:
            print('There are no items in this room\n')   
        pass     

    def room_check(self,direction):
        if direction == 'n': 
            return self.n_to
        elif direction == 's':
            return self.s_to
        elif direction == 'w':
            return self.w_to
        elif direction == 'e':
            return self.e_to
    

    def __str__(self):
        str_rep = f'You are now in the {self.name} room.\n {self.description} \n'
        return str_rep
    