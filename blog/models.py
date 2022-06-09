""" This file holds the database models for the blog post
and commenting within the Three Lions blog app
"""

from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Publish"))


class Post(models.Model):
    """
    Model for blog posts and all the fields included
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """orders blog posts by creation date"""
        ordering = ['-created_on']

    def __str__(self):
        """ returns the blog title"""
        return self.title

    def number_of_likes(self):
        """ returns the blog post like count"""
        return self.likes.count()


class Comment(models.Model):
    """
    Model for blog postcomments and all the fields included
    """

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """ orders comments by creation date"""
        ordering = ['created_on']

    def __str__(self):
        """ returns the comment and name of commenter"""
        return f"Comment {self.body} by {self.name}"
