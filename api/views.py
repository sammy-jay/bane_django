from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes

from .serializers import PostSerializer
from .models import Post

class PostView(APIView):
    # authentication_classes = [TokenAuthentication]
    
    @authentication_classes([TokenAuthentication])
    @permission_classes([IsAuthenticated])
    def get(self, request):
        print(request.user)
        posts = get_list_or_404(Post)
        serializer = PostSerializer(posts, many=True)
        return Response({"data": serializer.data})

    @permission_classes([IsAuthenticated])
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        serializer = PostSerializer(post)
        return Response({"data": serializer.data})

    @permission_classes([IsAuthenticated])
    def patch(self, request, id):
        post = get_object_or_404(Post, pk=id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([IsAuthenticated])
    def delete(self, request, id):
        post = get_object_or_404(Post, pk=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# context={'request': request}