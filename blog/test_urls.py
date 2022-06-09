""" Testing urls """

from django.test import TestCase
from django.urls import reverse, resolve
from blog import views

class TestUrls(TestCase):
    """ 
    Tests all my urls from urls.py
    """

    def 