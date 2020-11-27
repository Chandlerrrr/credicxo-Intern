from django.urls import path, include
from . import views

urlpatterns = [
      path('api/register', views.RegisterAPI.as_view()),
      path("list/users", views.ListUsers.as_view(), name="list_users"),
      path("create/user", views.CreateUser.as_view(), name="create_user"),
      path("forgot-password", views.ForgotPassword.as_view(), name="forgot-password"),
      path("change-password", views.ChangePassword.as_view(), name="change-password")
]

