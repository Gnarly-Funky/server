from django.conf.urls import url
from . import api

urlpatterns = [
    url('world/', api.get_world),
    url('init/', api.initialize),
    url('move/', api.move),
    url('say/', api.say),
]
