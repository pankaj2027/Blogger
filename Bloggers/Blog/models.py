from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    body = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    visitor_firstName = models.CharField(max_length=30)
    visitor_lastName = models.CharField(max_length=30)
    comment = models.CharField(max_length=500)
    status = models.CharField(max_length=50,choices=(('Approve', 'Approve'), ('Reject', 'Reject'),('Inprocess', 'Inprocess')),default="Inprocess")
    created_at = models.DateTimeField(auto_now_add=True)

