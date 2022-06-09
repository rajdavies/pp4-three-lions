from django.test import TestCase
from .forms import CommentForm, BlogForm


class TestCommentForm(TestCase):
    """ Unit test for comments form """
    def test_post_body_is_required(self):
        form = CommentForm(({'body': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(
            form.Meta.fields, ('body',)
        )


class TestBlogForm(TestCase):
    def test_post_title_is_required(self):
        form = BlogForm(({'title': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')
    
    def test_post_content_is_required(self):
        form = BlogForm(({'content': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')
    
    def test_fields_are_explicit_in_form_metaclass(self):
        form = BlogForm()
        self.assertEqual(
            form.Meta.fields, ('title', 'content', 'excerpt')
        )
    
