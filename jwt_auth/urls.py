from django.urls import path
from .views import LoginView, RegisterView, UserProfileView # TODO , ResetView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("profile/<int:pk>/", UserProfileView.as_view()),
    # TODO path("profile/<int:pk>/reset/", ResetView.as_view())
]