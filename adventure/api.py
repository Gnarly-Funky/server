import json
from rest_framework.decorators import api_view
from .models import *
from django.contrib.auth.models import User
from decouple import config
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
# from pusher import Pusher

# instantiate pusher
# pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))


@csrf_exempt
@api_view(["GET"])
def initialize(request):
    user = request.user
    player = user.player
    if not player.currentRoom:
        player.currentRoom = Room.objects.get(x=20, y=20).id
        player.save()
    player_id = player.id
    uuid = player.uuid
    room = Room.objects.get(id=player.currentRoom)
    return JsonResponse({'player_uuid': uuid, "room_uuid": room.uuid, "player_id": player_id, 'player_name': player.user.username, 'room_title': room.title, 'room_description': room.description}, safe=True)


@csrf_exempt
@api_view(["GET"])
def get_world(request):
    final = []
    world = Room.objects.all()
    for room in world:
        final.append({"id": room.id, "uuid": room.uuid, "title": room.title, "desc": room.description,
                      "touched": room.touched, "x": room.x, "y": room.y, "north": room.north, "south": room.south, "east": room.east, "west": room.west})
    return JsonResponse({"world": final}, safe=True)


@csrf_exempt
@api_view(["GET"])
def move(request):
    # player = request.user.player
    return JsonResponse({"new_room": "working"}, safe=True)
    # dirs = {"n": "north", "s": "south", "e": "east", "w": "west"}
    # reverse_dirs = {"n": "south", "s": "north", "e": "west", "w": "east"}
    # player = request.user.player
    # player_id = player.id
    # player_uuid = player.uuid
    # data = json.loads(request.body)
    # direction = data['direction']
    # room = player.room()
    # nextRoomID = None
    # if direction == "n":
    #     nextRoomID = room.n_to
    # elif direction == "s":
    #     nextRoomID = room.s_to
    # elif direction == "e":
    #     nextRoomID = room.e_to
    # elif direction == "w":
    #     nextRoomID = room.w_to
    # if nextRoomID is not None and nextRoomID > 0:
    #     nextRoom = Room.objects.get(id=nextRoomID)
    #     player.currentRoom = nextRoomID
    #     player.save()
    #     players = nextRoom.playerNames(player_id)
    #     currentPlayerUUIDs = room.playerUUIDs(player_id)
    #     nextPlayerUUIDs = nextRoom.playerUUIDs(player_id)
    # for p_uuid in currentPlayerUUIDs:
    #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has walked {dirs[direction]}.'})
    # for p_uuid in nextPlayerUUIDs:
    #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has entered from the {reverse_dirs[direction]}.'})
    #     return JsonResponse({'name': player.user.username, 'title': nextRoom.title, 'description': nextRoom.description, 'players': players, 'error_msg': ""}, safe=True)
    # else:
    #     players = room.playerNames(player_id)
    #     return JsonResponse({'name': player.user.username, 'title': room.title, 'description': room.description, 'players': players, 'error_msg': "You cannot move that way."}, safe=True)


@csrf_exempt
@api_view(["POST"])
def say(request):
    # IMPLEMENT
    return JsonResponse({'error': "Not yet implemented"}, safe=True, status=500)
