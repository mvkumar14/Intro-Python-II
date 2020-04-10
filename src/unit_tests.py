"""START ENVRIONMENT"""

from room import Room
from player import Player

# Two control scehmes:

# n, s, w, e
# WASD

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to rooms:
sword = Item('Sword','A Rusty Broadsword... Better than nothing I suppose?')
room['outside'].add_item(sword)

print(room['outside'])
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
my_player = Player(room['outside'])

"""END ENVIRONMENT"""

user_input = "get sword"
if len(user_input.split())==2:
        verb, noun = user_input.split()
        verb = verb.lower()
        noun = noun.lower()
        if verb == 'get' or verb == 'take':
            all_items = ['all','everything']
            if noun in all_items:
                my_player.get_all()
                pass
            else:
                my_player.get_item(noun)
                pass
        elif verb == 'drop' or verb == 'leave':
            my_player.drop_item(noun)
            pass
        else:
            print('test')
            pass