from rest_framework import status, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Blog, Comments
from .serializers import (BlogSerializer, CommentSerializer, UserSerializer,
                          ViewBlogWithCommentSerializer,CommentStatusSerializer)
from django.db.models import Q


# Blogger Registration

class BloggerRegistration(viewsets.ViewSet):
   
    def create(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Your registration has been completed Successfully!!"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Add,Update and delete a blog

class BlogDetails(viewsets.ViewSet):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = BlogSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response({'msg':"Your Blog Has Been Added Successfully!!"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):

        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Your Blog Has Been Updated Successfully!!"},status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response({'msg':"Your Blog Has Been Deleted Successfully!!"},status=status.HTTP_200_OK)

# Visitor  add the comment for a blog

class VisitorComments(viewsets.ViewSet):
   
    def create(self, request):
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Your comment has been added Successfully!!"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View the blog with comments
class ViewBlogWithComment(viewsets.ViewSet):

    def list(self,request):
        blog_data = Blog.objects.all()
        serializer = ViewBlogWithCommentSerializer(blog_data, many=True)
        return Response(serializer.data)    


# approve or reject the Comments
class CommentApproveReject(viewsets.ViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self,request):
        comment_data = Comments.objects.filter(blog__user = request.user, status="Inprocess")
        serializer= CommentStatusSerializer(comment_data, many=True)
        return Response(serializer.data) 
    
    def update(self,request,pk):
        comment_data = Comments.objects.get(pk=pk)
        serializer = CommentStatusSerializer(comment_data, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Comment is {}".format(request.data['status'])},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


