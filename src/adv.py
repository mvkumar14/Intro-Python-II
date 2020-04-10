from room import Room
from player import Player
from item import Item

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
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
def invalid_command():
    print('Not a valid command!\n\nCommands:\n[n s w e] to move \n[q]       to quit\n')


# Create a class for the parser itself? 

# Refactor the code so that the room can change the state of the parser
# So the room can give the parser details about the available actions of the room
# This requires that the parser itself is an object. 

# this shows the boundary between game designer and 
# game. The Designer thinks of the the game objects and the computer 
# objects as one. The tools of the designer to help program the game
# are no different programmatically compared to the objects in the game. 
# the tools themselves are objects used to communicate with game objects.

# this way you can reveal a virtual world and all you have to define is how 
# user inputs map to exploration of that world. The context/ the world details will
# change the behavior of the input parsing to the world.

# This matches/lines up nicely with the actions a user will take
# if you naturally progress through the game, the general actions you would
# take wouldn't be specific like " pee in a corner ", or 'stare really closely at the wall'
# or 'start breaking the wall'
# . It would be generic like move, interact with interactables and so on
# The "realism" is something that the person invites into the game, not the other 
# way around.

play = True
while play == True:
    current_room = my_player.current_room
    user_input = input("~~>:  ")
    print('-'*40)
    
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
        if verb == 'drop' or verb == 'leave':
            my_player.drop_item(noun)
            pass

        else:
            print('test')
            pass
    else:
        if user_input in ['n','s','w','e']:
            my_player.move(user_input)
            my_player.current_room.list_items()
        elif user_input == 'i' or user_input == 'inventory':
            my_player.print_inventory()
        elif user_input == 'q':
            play = False
        else:
            invalid_command()
        

