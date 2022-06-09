""" Unit testing views """

from django.test import TestCase

class TestViews(TestCase):
    """ Contains all the unit testing for my views
    each view is tested for the right response and template """

    def test_get_post_list(self):
        """ Unit test for PostList """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_get_post_detail(self):
        """ Tests if it gets the right response and template """
        response = self.client.get('post_detail')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
        