from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # User API endpoints
    path('api/register/', views.RegisterUserView.as_view(), name='register'),
    path('api/login', views.LoginUserView.as_view(), name='login'),
    path('api/logout', views.LogoutUserView.as_view(), name='logout'),
    path('api/user/', views.UserDetailView.as_view(), name='user-detail'),

   
]
