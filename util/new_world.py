# Comment this back in for production
from django.contrib.auth.models import User
from adventure.models import Player, Room  # Comment this back in for production
from random import randrange, choices

# Room.objects.all().delete()  # Comment this back in for production

titles = [
    [
        "Cloudy", "Dusty", "Warm", "Crumbling", "Dank", "Musty", "Moldy", "Funerial", "Dread", "Black", "Dark", "Grand", "Lost", "Forsaken", "Tormented", "Demented", "Rusty", "Decaying", "Reeking"
    ],
    [
        "Great Room", "Altar", "Hallway", "Chamber", "Cavern", "Expanse", "Overlook", "Library", "Laboratory", "Crypt", "Catacombs", "Shrine", "Sanctum", "Lair", "Temple", "Halls", "Cave"
    ],
    [
        "Death", "Annihiliation", "Torture", "Tranquility", "Secrets", "Chaos", "Desecration", "Blood", "Destruction", "Despair", "Ascendance", "Mortality"
    ]
]

descriptions = [
    [
        "Beams of light pierce through the clouds of dirt and dust lingering in the air.", "Every surface is covered in a thick layer of dust and grime.", "The warm air feels like it's sticking to your skin.", "The surface of the walls is chipping away.", "The room is oppressively humid, making it hard to breathe.", "A musty smell permeates the air around you.", "The smell of mold and mildew lingers in the air.", "The surroundings are adorned with offerings and honorific art, as if in preparation for a wake.", "You feel as though there's an ominous aura about this place.", "There's almost no light here. Everything is covered in black drapery.", "The room is filled with shadows, making it difficult to tell what you're looking at.", "The scale and adornment of this room is beyond anything you've seen before.", "This room looks as though it hasn't been used for anything in decades.", "It's as though this room hasn't been used in centuries.", "The room is filled with terrifying idols and symbols.", "The room is filled with ancient armor and weapons, all of them forgotten and slowly rusting away.", "It's as if the room itself is rotting away. The furniture, walls, floor, and everything else is falling to pieces.", "You have to hold your nose as soon as you enter. The stench in this room is overwhelming."
    ],
    [
        "You're in a massive room. Each footsteps echo off distant walls.", "There's an altar in the room, covered in symbols you can't read and idols you don't recognize.", "You're in a hallway, most doors are blocked.", "You've entered a large chambers, filled wall to wall with seating. It must have been used for grand debates.", "Your surroundings don't resemble those of a room. There are stalactites hanging from the ceiling, as if you're in a cavern.", "You've entered an absolutely massive room. It reaches out in every direction.", "You're on an overarching balcony that looks down on a great arena.", "The smell of old paper fills the room, and rows of bookshelves neatly go from wall to wall.", "Beakers and burners litter a series of desks. Terrifying experiments sit inside jars on shelves.", "The room is lined with stone coffins, each engraved with names in an unknown language.", "The walls themselves hold countless graves, each marked with the names of the dead.", "In the center of the room stands a grand statue of an ancient goddess.", "The room is peaceful. You get the feeling that all is right in the world.", "A serpentene decoration addorns the room. Gold and treasure is piled in the corner.", "A broken altar sits in the corner. Melted and lit candles line the walls.", "You've entered a series of halls. Most doors are blocked.", "Your surroundings don't resemble those of a room. There are stalactites hanging from the ceiling, as if you're in a cave."
    ],
    [
        "A feeling of death hangs over the room, and decaying bodies lie in the corner.", "An oppressive feeling of the annihilation comes over you.", "A rack and stretching tools sit in the corner next to a pile of bones.", "An inner peace settles over you.", "There is a massive X in the middle of the room. Echoes of ancient secrets bounce off the walls.", "You find it hard to think. Which way was out, again?", "Angry red writing covers the walls, and the adornments seem out of place.", "There is blood splattered around the room.", "The ground is broken up beneath your feet.", "You begin to feel despair that this is all you'll ever know.'", "Soft choir chanting drifts down from somewhere.", "The oppressive air feeds your feeling of impending doom."
    ]
]


def create_info():
    title = ""
    desc = ""
    for i in range(3):
        num = randrange(0, len(titles[i]))
        if len(title) is 0:
            title += titles[i][num]
            desc += descriptions[i][num]
        elif i == 2:
            title += " of " + titles[i][num]
            desc += " " + descriptions[i][num]
        else:
            title += " " + titles[i][num]
            desc = descriptions[i][num] + " " + desc
    return [title, desc]

# PART ! - --- INSTANTIATE NEW ROOMS IN GAME BOARD
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

def gen_room(x_val, y_val):
    title_desc = create_info()
    room = Room(x=x_val, y=y_val,
                title=title_desc[0], description=title_desc[1])
    return room


# Generate Map
new_world = [[gen_room(i, j) for j in range(0, 41)]
             for i in range(0, 41)]


def walker(current_place, count, odds=[75, 75, 75, 75]):
    rand_num = choices([0, 1, 2, 3], weights=odds)[0]
    new_world[current_place[0]][current_place[1]].touched = True
    if count == 0:
        return None
    # North
    if rand_num == 0:
        new_odds = [odds[0]+20, odds[1], odds[2]+2, odds[3]+2]
        if current_place[1] == 0:
            return None
        new_world[current_place[0]][current_place[1]].connectRooms("north")
        new_world[current_place[0]][current_place[1]-1].connectRooms("south")
        walker([current_place[0], current_place[1]-1], count - 1, new_odds)
    # South
    elif rand_num == 1:
        new_odds = [odds[0], odds[1]+20, odds[2]+2, odds[3]+2]
        # Hard coded, change later
        if current_place[1] == len(new_world)-1:
            return None
        new_world[current_place[0]][current_place[1]].connectRooms("south")
        new_world[current_place[0]][current_place[1]+1].connectRooms("north")
        walker([current_place[0], current_place[1]+1], count - 1, new_odds)
    # East
    elif rand_num == 2:
        new_odds = [odds[0]+2, odds[1]+2, odds[2]+20, odds[3]]
        # Hard coded, change later
        if current_place[0] == len(new_world)-1:
            return None
        new_world[current_place[0]][current_place[1]].connectRooms("east")
        new_world[current_place[0]+1][current_place[1]].connectRooms("west")
        walker([current_place[0]+1, current_place[1]], count - 1, new_odds)
    # West
    elif rand_num == 3:
        new_odds = [odds[0]+2, odds[1]+2, odds[2], odds[3]+20]
        if current_place[0] == 0:
            return None
        new_world[current_place[0]][current_place[1]].connectRooms("west")
        new_world[current_place[0]-1][current_place[1]].connectRooms("east")
        walker([current_place[0]-1, current_place[1]], count - 1, new_odds)


for i in range(0, 20):
    walker([len(new_world)//2, len(new_world)//2], 200)

count = 0

for i in range(0, len(new_world)):
    for j in range(0, len(new_world)):
        if new_world[j][i].touched:
            room = new_world[j][i]
            room.save()
            count += 1
            print(count)

# with open("test.txt", "w") as text:
#     for i in range(0, len(new_world)):
#         for j in range(0, len(new_world)):
#             if new_world[j][i].touched:
#                 text.write(" ")
#             else:
#                 text.write("#")
#         text.write("\n")
#     text.close()

players = Player.objects.all()
for p in players:
    root_room = new_world[len(new_world)//2, len(new_world)//2]
    p.currentRoom = root_room.uuid
    p.save()
