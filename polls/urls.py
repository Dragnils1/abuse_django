from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage, name="mainPage"),
    path('about/', views.about, name="about"),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
]
