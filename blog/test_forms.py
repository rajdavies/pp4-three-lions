from django.test import TestCase
from .forms import CommentForm, BlogForm


class TestCommentForm(TestCase):
    """ Unit test for comments form """
    def test_post_body_is_required(self):
        """ tests if post body is required """
        form = CommentForm(({'body': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """ tests if fields are explicit in comment form """
        form = CommentForm()
        self.assertEqual(
            form.Meta.fields, ('body',)
        )


class TestBlogForm(TestCase):
    """ Unit test for blog form """
    def test_post_title_is_required(self):
        """ tests if post title is required """
        form = BlogForm(({'title': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_post_content_is_required(self):
        """ tests if post content is required """
        form = BlogForm(({'content': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        """ tests if fields are explicit in blog form """
        form = BlogForm()
        self.assertEqual(
            form.Meta.fields, ('title', 'content', 'excerpt')
        )
