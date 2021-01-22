from django.urls import path
from .views import FarmerSignUpView, signup, DecisonMakerSignUpView, profile, farmers_view, decisionmarkers_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", signup, name="signup"),
    path("farmers/", farmers_view, name="farmers"),
    path("decision_makers/", decisionmarkers_view, name="decisionmakers"),
    path("profile/", profile, name="profile"),
    path("signup/", signup, name="signup"),
    path("signup/decisionmaker", DecisonMakerSignUpView.as_view(), name="decisionmaker-signup"),
    path("signup/farmer", FarmerSignUpView.as_view(), name="farmer-signup"),

    # authentication
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # password change  
    path("password_change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),

    # reset password
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete")

]
