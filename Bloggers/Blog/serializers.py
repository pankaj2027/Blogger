from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Blog, Comments


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['username','email','first_name','last_name','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','title','sub_title','body']
        extra_kwargs = {'id': {'read_only': True}}

 
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['blog','visitor_firstName','visitor_lastName','comment']


class CommentStatusSerializer(serializers.ModelSerializer):
    blog = serializers.CharField(source='blog.title',read_only=True)
    class Meta:
        model = Comments
        fields = ['id','blog','visitor_firstName','visitor_lastName','comment','status']
        read_only_fields = ('id','visitor_firstName','visitor_lastName','comment')


class ViewBlogWithCommentSerializer(serializers.ModelSerializer):
    
    comments = serializers.SerializerMethodField('get_comments')
    
    def get_comments(self, blog):
        qs = Comments.objects.filter(status="Approve", blog=blog)
        serializer = CommentSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = Blog
        fields = ['title','sub_title','body','comments']

    
    

    
