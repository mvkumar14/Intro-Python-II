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

def error_no_room():
    print("There is no room in that direction. Try again!\n")

play = True
while play == True:
    current_room = my_player.current_room
    user_input = input("Type a direction:  ")
    print('\n')
    if user_input in ['n','s','w','e']:
        new_room = current_room.room_check(user_input)
        if new_room:
            my_player.move(new_room)
            print(new_room)
            new_room.list_items()
        else:
            error_no_room()
    elif user_input == 'q':
        play = False
    else:
        print('Not a valid command! \n Commands:\nn s w e to move \nq to quit')

