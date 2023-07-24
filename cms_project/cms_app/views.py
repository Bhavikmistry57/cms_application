from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Post, Like
from .serializers import UserSerializer, PostSerializer, LikeSerializer
from .permissions import IsOwnerOrReadOnly
from django.http.response import Http404 

class UserAPIView(APIView):

        # READ a single user
        def get_object(self, pk):
            try:
                data = User.objects.get(pk=pk)
                return data
            except User.DoesNotExist:
                raise Http404

        def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = UserSerializer(data)
                
            else:
                data = User.objects.all()
                serializer = UserSerializer(data, many=True)
            return Response(serializer.data)
            
        def post(self, request, format=None):
            data = request.data
            serializer = UserSerializer(data=data)

            # Check if the data passed is valid
            serializer.is_valid(raise_exception=True)
            # Create User in the DB
            serializer.save()

            # Return Response to User
            response = Response()
            response.data = {
                'message': 'User Created Successfully',
                'data': serializer.data
            }

            return response

        def put(self, request, pk=None, format=None):
            # Get the user to update
            user_to_update = User.objects.get(pk=pk)

            # Pass the instance to update to the serializer, and the data and also partial to the serializer
            # Passing partial will allow us to update without passing the entire user object
            serializer = UserSerializer(instance=user_to_update,data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = Response()
            response.data = {
                'message': 'User Updated Successfully',
                'data': serializer.data
            }
            return response

        def delete(self, request, pk, format=None):
            user_to_delete =  User.objects.get(pk=pk)

            # delete the user
            user_to_delete.delete()

            return Response({
                'message': 'User Deleted Successfully'
            })


class PostAPIView(APIView):

        permission_classes = [IsOwnerOrReadOnly]
        # READ a single Post
        def get_object(self, pk):
            try:
                data = Post.objects.get(pk=pk)
                return data
            except Post.DoesNotExist:
                raise Http404

        def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = PostSerializer(data)
                
            else:
                data = Post.objects.all()
                serializer = PostSerializer(data, many=True)
            return Response(serializer.data)
            
        def post(self, request, format=None):
            data = request.data
            serializer = PostSerializer(data=data)

            # Check if the data passed is valid
            serializer.is_valid(raise_exception=True)
            # Create post in the DB
            serializer.save()

            # Return Response to Post
            response = Response()
            response.data = {
                'message': 'Post Created Successfully',
                'data': serializer.data
            }

            return response

        def put(self, request, pk=None, format=None):
            # Get the post to update
            post_to_update = Post.objects.get(pk=pk)

            # Pass the instance to update to the serializer, and the data and also partial to the serializer
            # Passing partial will allow us to update without passing the entire post object
            serializer = PostSerializer(instance=post_to_update,data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = Response()
            response.data = {
                'message': 'Post Updated Successfully',
                'data': serializer.data
            }
            return response

        def delete(self, request, pk, format=None):
            post_to_delete =  Post.objects.get(pk=pk)

            # delete the post
            post_to_delete.delete()

            return Response({
                'message': 'Post Deleted Successfully'
            })


class LikeAPIView(APIView):

        # READ a single like
        def get_object(self, pk):
            try:
                data = Like.objects.get(pk=pk)
                return data
            except Like.DoesNotExist:
                raise Http404

        def get(self, request, pk=None, format=None):
            if pk:
                data = self.get_object(pk)
                serializer = LikeSerializer(data)
                
            else:
                data = Like.objects.all()
                serializer = LikeSerializer(data, many=True)
            return Response(serializer.data)
            
        def post(self, request, format=None):
            data = request.data
            serializer = LikeSerializer(data=data)

            # Check if the data passed is valid
            serializer.is_valid(raise_exception=True)
            # Create like in the DB
            serializer.save()

            # Return Response to Post
            response = Response()
            response.data = {
                'message': 'Liked Successfully',
                'data': serializer.data
            }

            return response

        def put(self, request, pk=None, format=None):
            # Get the like to update
            like_to_update = Like.objects.get(pk=pk)

            # Pass the instance to update to the serializer, and the data and also partial to the serializer
            # Passing partial will allow us to update without passing the entire like object
            serializer = LikeSerializer(instance=like_to_update,data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = Response()
            response.data = {
                'message': 'Like Updated Successfully',
                'data': serializer.data
            }
            return response

        def delete(self, request, pk, format=None):
            like_to_delete =  Like.objects.get(pk=pk)

            # delete the todo
            like_to_delete.delete()

            return Response({
                'message': 'Like Deleted Successfully'
            })
        

