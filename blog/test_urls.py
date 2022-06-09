""" Testing urls """

from django.test import TestCase
from django.urls import reverse, resolve
from blog import views


class TestUrls(TestCase):
    """
    Tests all my urls from urls.py
    """

    def test_home_url_resolves(self):
        """ tests if home url resolves """
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, views.PostList)

    def test_post_detail_url_resolves(self):
        """ tests if post_detail url resolves """
        url = reverse('post_detail', args=[12345678901234567890])
        self.assertEqual(resolve(url).func.view_class, views.PostDetail)
    
    def test_post_like_url_resolves(self):
        """ tests if post_like url resolves """
        url = reverse('post_like', args=[12345678901234567890])
        self.assertEqual(resolve(url).func.view_class, views.PostLike)
    
    def test_create_post_url_resolves(self):
        """ tests if home url resolves """
        url = reverse('create_post')
        self.assertEqual(resolve(url).func.view_class, views.CreatePost)
