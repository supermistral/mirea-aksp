from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('room/<str:invite_code>/<str:username>/', views.chatroom, name='chatroom'),
]
