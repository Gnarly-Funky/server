import json
from rest_framework.decorators import api_view
from .models import *
from django.contrib.auth.models import User
from decouple import config
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from pusher import Pusher


# instantiate pusher
pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))


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
    other_players = []
    players = Player.objects.all()
    for p in players:
        if p.currentRoom == player.currentRoom:
            if p.id != player_id:
                other_players.append(p.user.username)
    return JsonResponse({'player_uuid': uuid, "room_uuid": room.uuid, "player_id": player_id, 'player_name': player.user.username, "room_id": room.id, "room_x": room.x, "room_y": room.y, 'room_title': room.title, 'room_description': room.description, "other_players": other_players}, safe=True)


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
@api_view(["POST"])
def move(request):
    data = json.loads(request.body)
    current_player = Player.objects.get(uuid=request.user.player.uuid)
    current_player.currentRoom = data["room_id"]
    current_player.save()
    other_players = []
    players = Player.objects.all()
    for p in players:
        if p.currentRoom == current_player.currentRoom:
            if p.id != current_player.id:
                other_players.append(p.user.username)
    return JsonResponse({"new_room": current_player.currentRoom, "other_players": other_players}, safe=True)


@csrf_exempt
@api_view(["POST"])
def say(request):
    # IMPLEMENT
    pusher.trigger(u'a_channel', u'an_event', {u'name': request.user.username, u'message': request.POST['message']})
    return HttpResponse("done");
    # return JsonResponse({'error': "Not yet implemented"}, safe=True, status=500)
