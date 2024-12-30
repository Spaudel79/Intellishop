from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout

User = get_user_model()



class LogoutUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Log the user out
        logout(request)
        return Response({"message": "Logged out successfully"}, status=200)

# User registration view
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to register

# View for getting user details
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can view their details

    def get_object(self):
        return self.request.user  # Retrieve the currently authenticated user

# Token generation (login) view
class LoginUserView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        print(email)
        print('email',email)
        print('password:',password)
        # breakpoint()
        user = User.objects.filter(email=email).first()
        if user and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid credentials"}, status=400)

