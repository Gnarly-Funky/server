# Comment this back in for production
from django.contrib.auth.models import User
from adventure.models import Player, Room  # Comment this back in for production
from random import randrange, choices

# Room.objects.all().delete()  # Comment this back in for production

# titles = [
#     [
#         "Cloudy", "Dusty", "Warm", "Crumbling", "Dank", "Musty", "Moldy", "Funerial", "Dread", "Lost", "Black", "Dark", "Grand", "Narrow", "Lost", "Forsaken", "Gauntlet", "Mighty", "Tormented", "Demented", "Brick", "Rusty", "Decaying", "Reeking"
#     ],
#     [
#         "Great Room", "Alter", "Hallway", "Chamber", "Cavern", "Expanse", "Overlook", "Foyer", "Library", "Laboratory", "Crypt", "Catacombs", "Archway", "Shrine", "Sanctum", "Lair", "Temple", "Halls", "Cave", "Divide", "Quicksand", "Realm"
#     ],
#     [
#         "Death", "Annihiliation", "Torture", "Tranquility", "Secrets", "Chaos", "Desecration", "Blood", "Destruction", "Despair", "Ascendance", "Mortality"
#     ]
# ]


# PART ! ---- INSTANTIATE NEW ROOMS IN GAME BOARD
# Comment this class out for production run
# class Room:
#     def __init__(self, x, y):
#         self.title = self.create_title()
#         self.desc = ""

#         self.touched = False

#         self.x = x
#         self.y = y

#         self.north = False
#         self.south = False
#         self.east = False
#         self.west = False

#     def create_title(self):
#         str = ""
#         for i in range(3):
#             num = randrange(0, len(titles[i]))
#             if len(str) is 0:
#                 str += titles[i][num]
#             elif i == 2:
#                 str += " of " + titles[i][num]
#             else:
#                 str += " " + titles[i][num]
#         return str

#     def connectRooms(self, direction):
#         if direction == "north":
#             self.north = True
#         elif direction == "south":
#             self.north = True
#         elif direction == "east":
#             self.east = True
#         elif direction == "west":
#             self.west = True
#         else:
#             print("Invalid direction")
#             return

def save_room(x, y):
    room = Room()
    room.save()
    room.initialize_room(x, y)
    return room


# Generate Map
new_world = [[save_room(j, i) for j in range(0, 20)] for i in range(0, 20)]


def walker(current_place, count, odds=[75, 75, 75, 75]):
    rand_num = choices([0, 1, 2, 3], weights=odds)[0]
    new_world[current_place[0]][current_place[1]].touched = True
    if count == 0:
        return None
    # North
    if rand_num == 0:
        new_odds = [odds[0]+1, odds[1], odds[2], odds[3]]
        if current_place[1] == 0:
            return None
        new_world[current_place[0]][current_place[1]].connectRooms("north")
        new_world[current_place[0]][current_place[1]-1].connectRooms("south")
        walker([current_place[0], current_place[1]-1], count - 1, new_odds)
    # South
    elif rand_num == 1:
        new_odds = [odds[0], odds[1]+1, odds[2], odds[3]]
        # Hard coded, change later
        if current_place[1] == len(new_world)-1:
            return None
        new_world[current_place[0]][current_place[1]].connectRooms("south")
        new_world[current_place[0]][current_place[1]+1].connectRooms("north")
        walker([current_place[0], current_place[1]+1], count - 1, new_odds)
    # East
    elif rand_num == 2:
        new_odds = [odds[0], odds[1], odds[2]+1, odds[3]]
        # Hard coded, change later
        if current_place[0] == len(new_world)-1:
            return None
        new_world[current_place[0]][current_place[1]].connectRooms("east")
        new_world[current_place[0]+1][current_place[1]].connectRooms("west")
        walker([current_place[0]+1, current_place[1]], count - 1, new_odds)
    # West
    elif rand_num == 3:
        new_odds = [odds[0], odds[1], odds[2], odds[3]+1]
        if current_place[0] == 0:
            return None
        new_world[current_place[0]][current_place[1]].connectRooms("west")
        new_world[current_place[0]-1][current_place[1]].connectRooms("east")
        walker([current_place[0]-1, current_place[1]], count - 1, new_odds)


for i in range(0, 20):
    walker([len(new_world)//2, len(new_world)//2], 100)

# with open("test.txt", "w") as text:
#     for i in range(0, len(new_world)):
#         for j in range(0, len(new_world)):
#             if new_world[j][i].touched:
#                 text.write(" ")
#             else:
#                 text.write("#")
#         text.write("\n")
#     text.close()
