from django.urls import include, path
from rest_framework import routers

from .views import (BlogDetails, BloggerRegistration, ViewBlogWithComment,
                    VisitorComments,CommentApproveReject)

router = routers.DefaultRouter()
router.register('registration', BloggerRegistration, basename='registration')
router.register('blogdetail', BlogDetails, basename='blog')
router.register('addcomment', VisitorComments, basename='addcomment')
router.register('commentapprovereject', CommentApproveReject, basename='commentapprovereject')
router.register('viewblogwithcomment', ViewBlogWithComment, basename='viewcomment')



urlpatterns = [
   path('', include(router.urls)),
]
