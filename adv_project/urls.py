from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import include
from pusherchat import views
from adventure import api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
    path('chat/', views.chat),
    path('ajax/chat/', api.say),
]
