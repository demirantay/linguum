from django.urls import path
from . import views

urlpatterns = [
    # Edit Profile
    path("profile/settings/edit_profile/", views.profile_settings_edit_profile, name="profile_settings_edit_profile"),
    # Change Password
    path("profile/settings/change_password/", views.profile_settings_change_password, name="profile_settings_change_password"),
    # Email and SMS
    path("profile/settings/email_sms/", views.profile_settings_email_sms, name="profile_settings_email_sms"),
]
