from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup_user, name="signup_user"),
    path("display", views.disp_users, name="disp_users"),
    path("login", views.login_user, name="login_user"),
    path("logout", views.logout_user, name="logout_user"),
    path("newproj", views.new_proj, name="new_proj"),
    path("disproj", views.disp_proj, name="disp_proj"),
    path("update", views.update_user, name="update_user"),
    path("newappr", views.new_appr, name="new_appr"),
    path("dispappr", views.disp_appr, name="disp_appr"),
    path("newremk", views.new_remk, name="new_remk"),
    path("dispremk", views.disp_remk, name="disp_remk"),
    path("resetPassword/" , auth_views.PasswordResetView.as_view(template_name = 'passwordReset.html')),
    path("resetPassword/success/" , auth_views.PasswordResetDoneView.as_view(template_name = 'passwordResetSuccess.html')),
    path("resetPassword/confirm/<uidb64>/<token>" , auth_views.PasswordResetConfirmView.as_view(template_name = 'passwordResetConfirm.html')),


    ]
