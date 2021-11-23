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
    path("admindash",views.admin_dash,name="admin_dash"),
    path("hrdash",views.hr_dash,name="hr_dash"),
    path("empdash",views.emp_dash,name="emp_dash"),
    path("adminupdate",views.admin_update,name='admin_update'),
    path("delempform",views.del_emp_form, name='del_emp_form'),
    path("delprojform",views.del_proj_form, name='del_proj_form'),
    path("delproj",views.del_proj,name='del_proj'),
    path("delemp",views.del_emp,name='del_emp'),
    path("resetPassword/" , auth_views.PasswordResetView.as_view(template_name = 'passwordReset.html') , name = "password_reset"),
    path("resetPassword/success/" , auth_views.PasswordResetDoneView.as_view(template_name = 'passwordResetSuccess.html') ,name = "password_reset_done" ),
    path("resetPassword/confirm/<uidb64>/<token>" , auth_views.PasswordResetConfirmView.as_view(template_name = 'passwordResetConfirm.html') , name = "password_reset_confirm"),
    path("resetPassword/confirm/" , auth_views.PasswordResetCompleteView.as_view(template_name = 'passwordResetComplete.html') , name = "password_reset_complete"),

    ]
