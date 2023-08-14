from django.urls import path

from . import views, auth

urlpatterns = [
    # auth urls
    path('auth/register', auth.UserRegistrationView.as_view()),
    path('auth/login', auth.UserLoginView.as_view()),
    path('auth/logout', auth.UserLogoutView.as_view()),

    # posts urls
    path('posts/', views.PostView.as_view()),
    path('posts/<int:id>', views.PostDetailView.as_view()),
]
