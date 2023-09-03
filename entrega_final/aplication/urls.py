from django.contrib import admin
from django.urls import path 
from .views import * 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path ('', home, name="home"), 
    path('home', home, name = "home"),
    path('about', about, name = "about"),
    path('post', postForm, name = "post"),
    path('categories', categories, name="categories"),
    path('updatePost/<id_post>', updatePost, name="updatePost"),
    path('deletePost/<id_post>/', deletePost, name="deletePost"),
    path('login/', userLogin, name="login" ),
    path('logout/', LogoutView.as_view(template_name="aplication/logout.html"), name="logout" ),
    path('register/', userRegister, name="register" ),
    path('edit_profile/', editarPerfil, name="edit_profile" ),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar" ),
]

