from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from random import randrange
import uuid

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


class Room(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT TITLE")
    description = models.CharField(
        max_length=500, default="DEFAULT DESCRIPTION")

    touched = models.BooleanField(default=False)

    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)

    north = models.BooleanField(default=False)
    south = models.BooleanField(default=False)
    east = models.BooleanField(default=False)
    west = models.BooleanField(default=False)

    def __init__(self, x=0, y=0):
        self.title = self.create_title()
        self.x = x
        self.y = y

    def create_title(self):
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

    def connectRooms(self, direction):
        if direction == "north":
            self.north = True
        elif direction == "south":
            self.north = True
        elif direction == "east":
            self.east = True
        elif direction == "west":
            self.west = True
        else:
            print("Invalid direction")
            return
        self.save()

    # def playerNames(self, currentPlayerID):
    #     return [p.user.username for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]

    # def playerUUIDs(self, currentPlayerID):
    #     return [p.uuid for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currentRoom = models.IntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    def initialize(self):
        if self.currentRoom == 0:
            self.currentRoom = Room.objects.first().id
            self.save()

    def room(self):
        try:
            return Room.objects.get(id=self.currentRoom)
        except Room.DoesNotExist:
            self.initialize()
            return self.room()


@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
        Token.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):
    instance.player.save()
