from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#render library for returning views to the browser
from django.shortcuts import render
#decorator to make a function only accessible to registered users
from django.contrib.auth.decorators import login_required
#import the user library
from pusher import Pusher
from decouple import config



# replace the xxx with your app_id, key and secret respectively
# instantate the pusher class
pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))# Create your views here.
#login required to access this page. will redirect to admin login page.
@login_required(login_url='/admin/login/')
def chat(request):
    print('logged in and in the chat')
    return render(request,"chat.html");

# Don't need it, it's in api.py as the say function
# @csrf_exempt
# def broadcast(request):
#     pusher.trigger(u'a_channel', u'an_event', {u'name': request.user.username, u'message': request.POST['message']})
#     return HttpResponse("done");


