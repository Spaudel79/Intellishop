from django.urls import path
from . import views
from .views import *

urlpatterns = [
    # User API endpoints
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('user/', views.UserDetailView.as_view(), name='user-detail'),

   
]
