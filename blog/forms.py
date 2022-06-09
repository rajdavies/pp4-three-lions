from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    """ Form for user to post comments on blog posts """
    class Meta:
        model = Comment
        fields = ('body',)


class BlogForm(forms.ModelForm):
    """ Form for user to create their own blog post """
    class Meta:
        model = Post
        fields = '('title', 'content', 'excerpt',)'
