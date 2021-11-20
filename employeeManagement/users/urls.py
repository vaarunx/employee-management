from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup_user, name="signup_user"),
    path("display", views.disp_users, name="disp_users"),
    path("login", views.login_user, name="login_user"),
    path("logout", views.logout_user, name="logout_user"),
    path("newproj", views.new_proj, name="new_proj"),
    path("disproj", views.disp_proj, name="disp_proj"),
    ]
