from django.urls import path    
from . import views


urlpatterns = [
    path("", views.home, name="home" ),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerPage, name="register"),
    path("room/<int:id>/", views.room, name="room"),
    path("create-room/", views.createRoom, name="create-room"),
    path("update-room/<int:id>/", views.updateRoom, name="update-room"),
    path("delete-room/<int:id>/", views.deleteRoom, name="delete-room"),
    path("delete-message/<int:id>/", views.deleteMessage, name="delete-message")
]

