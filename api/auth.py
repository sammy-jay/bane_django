from django.contrib.auth import login, authenticate, logout
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            avatar = request.data.get('avatar')
            if avatar:
                serializer.validated_data['avatar'] = avatar
            serializer.save()
            return Response({"data": serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        

        if user is not None:
            login(request, user)
            serializer = UserSerializer(user)
            return Response({"data": serializer.data})
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"msg": "success"})