""" Unit testing views """

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment

class TestViews(TestCase):
    """ Contains all the unit testing for my views
    each view is tested for the right response and template """

    def test_get_post_list(self):
        """ Unit test for PostList """
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_create_post(self):
        """ Unit test for CreatePost """
        client = Client()
        response = client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_post.html')
