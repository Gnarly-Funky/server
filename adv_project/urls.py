from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import include
from pusherchat import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/adv/', include('adventure.urls')),
    re_path(r'chat/', views.chat),
    re_path(r'^ajax/chat/$', views.broadcast),
]
