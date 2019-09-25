from random import randrange

titles = [
    [
        "Cloudy", "Dusty", "Warm", "Crumbling", "Dank", "Musty", "Moldy", "Funerial", "Dread", "Lost", "Black", "Dark", "Grand", "Narrow", "Lost", "Forsaken", "Gauntlet", "Mighty", "Tormented", "Demented", "Brick", "Rusty", "Decaying", "Reeking"
    ],
    [
        "Great Room", "Alter", "Hallway", "Chamber", "Cavern", "Expanse", "Overlook", "Foyer", "Library", "Laboratory", "Crypt", "Catacombs", "Archway", "Shrine", "Sanctum", "Lair", "Temple", "Halls", "Cave", "Divide", "Quicksand", "Realm"
    ],
    [
        "Death", "Annihiliation", "Torture", "Tranquility", "Secrets", "Chaos", "Desecration", "Blood", "Destruction", "Despair", "Ascendance", "Mortality"
    ]
]

#TODO
#front end display algo
#main images
#minimap

#Backend todo
#random descriptions
#store players in room
#JSONify new_world
#figure out sessions stuff
#write move

#Chat?

def gen():
    str = ""
    for i in range(3):
        num = randrange(0, len(titles[i]))
        if len(str) is 0:
            str += titles[i][num]
        elif i == 2:
            str += " of " + titles[i][num]
        else:
            str += " " + titles[i][num]
    return str

class Room():
    def __init__(self):
        self.title = gen()
        self.desc = "asdf"

        self.touched = False

        self.north = False
        self.south = False
        self.east = False
        self.west = False


new_world = [[Room() for j in range(0,101)] for i in range(0,101)]

#server sends new_world to client
#server sends current player position to client
#server -> client
#
#when you move
#send prev coords
#send current coords [50,100]
#pick up an item
#what item, what coords
#client -> server

#Generate links starting from

from random import choices

#Odds = [N, S, E, W]
def walker(current_place, count, odds = [75,75,75,75]):
    rand_num = choices([0,1,2,3], weights = odds)[0]

    new_world[current_place[0]][current_place[1]].touched = True

    if count == 0:
        return
    #North
    if rand_num == 0:
        new_odds = [odds[0]+1, odds[1], odds[2], odds[3]]
        if current_place[1] == 0:
            return
        new_world[current_place[0]][current_place[1]].north = True
        new_world[current_place[0]][current_place[1]-1].south = True
        walker([current_place[0], current_place[1]-1], count - 1, new_odds)

    #South
    elif rand_num == 1:
        new_odds = [odds[0], odds[1]+1, odds[2], odds[3]]
        #Hard coded, change later
        if current_place[1] == len(new_world)-1:
            return
        new_world[current_place[0]][current_place[1]].south = True
        new_world[current_place[0]][current_place[1]+1].north = True
        walker([current_place[0], current_place[1]+1], count - 1, new_odds)

    #East
    elif rand_num == 2:
        new_odds = [odds[0], odds[1], odds[2]+1, odds[3]]
        #Hard coded, change later
        if current_place[0] == len(new_world)-1:
            return
        new_world[current_place[0]][current_place[1]].east = True
        new_world[current_place[0]+1][current_place[1]].west = True
        walker([current_place[0]+1, current_place[1]], count - 1, new_odds)

    #West
    elif rand_num == 3:
        new_odds = [odds[0], odds[1], odds[2], odds[3]+1]
        if current_place[0] == 0:
            return
        new_world[current_place[0]][current_place[1]].west = True
        new_world[current_place[0]-1][current_place[1]].east = True
        walker([current_place[0]-1, current_place[1]], count - 1, new_odds)

for i in range(0,20):
    walker([len(new_world)//2, len(new_world)//2], 500)

with open("test.txt", "w") as text:
    for i in range(0,len(new_world)):
        for j in range(0,len(new_world)):
            if new_world[j][i].touched:
                text.write(" ")
            else:
                text.write("#")
        text.write("\n")
    text.close()