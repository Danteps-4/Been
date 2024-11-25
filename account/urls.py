from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "account"

urlpatterns = [
    path("register/", views.sign_up, name="sign_up"),
    path("logout/", views.log_out, name="logout"),
    path("profile/view/", views.profile_view, name="profile_view"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
    path("profile/view-visits/", views.profile_view_visits, name="profile_view_visits"),
    path("profile/add-friend/<slug:profile_slug>/", views.add_friend, name="add_friend"),
    path("profile/view-friends/", views.view_friends, name="view_friends"),
    path("profile/view-friends/delete/<slug:friend>/", views.delete_friend, name="delete_friend"),

    # Reset Password
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]