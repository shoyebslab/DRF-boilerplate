from django.urls import path

from apps.users.views.user import (
    UserDetailView,
    UserListCreateView,
)

urlpatterns = [
    path("", UserListCreateView.as_view(), name="user-list"),
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),
]
