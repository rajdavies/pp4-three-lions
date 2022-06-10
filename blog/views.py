from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post
from .forms import CommentForm, BlogForm


class PostList(generic.ListView):
    """ displays blog post list """
    model = Post
    queryset = Post.objects.filter(approved=True).order_by('created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    """ displays blog post detail """
    def get(self, request, slug, *args, **kwargs):
        """ gets the post detail """
        queryset = Post.objects.filter(approved=True)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """ posts comments """
        queryset = Post.objects.filter(approved=True)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):
    """ posts likes or removes likes from the post detail """
    def post(self, request, slug):
        """ function allows user to like or unlike posts """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class CreatePost(View):
    """
    This class contains the get method to provide the blog post
    form to enable the user to create a blog post.
    This class contians the post method allowing the user to
    submit their blog post to the admin for verification.
    """

    def get(self, request, *args, **kwargs):
        """
        the get method which displays the blog post
        form to the user.
        """
        blog_form = BlogForm()
        context = {'blog_form': blog_form}
        return render(request, 'create_post.html', context)

    def post(self, request, *args, **kwargs):
        """
        This post method submits the blog post
        to be accepted in the admin area.
        """

        blog_form = BlogForm(request.POST, request.FILES)

        if blog_form.is_valid():
            form = blog_form.save(commit=False)
            form.author = User.objects.get(username=request.user.username)
            form.slug = form.title.replace(" ", "-")
            messages.success(
                request, 'Your post has been submitted and awaiting approval.'
            )
            form.save()
        return redirect('home')


def user_posts(request):
    """ authenticated user can view and manage their created posts """

    logged_in_user = request.user
    logged_in_user_posts = Post.objects.filter(author=logged_in_user)
    return render(request, 'user_posts.html', {'posts': logged_in_user_posts})


def edit_post(request, post_id):
    """ authenticated users can edit their own blog posts """
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, instance=post)
        if blog_form.is_valid():
            form = blog_form.save(commit=False)
            form.approved = False
            messages.success(
                request, 'Updated post has been submitted for admin approval'
            )
            form.save()
            return redirect('user_posts')
    blog_form = BlogForm(instance=post)
    context = {'blog_form': blog_form}
    return render(request, 'edit_posts.html', context)


def delete_post(request, post_id):
    """ authenticated users can delete their own posts """
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    messages.success(request, 'Post successfully deleted.')
    return redirect('user_posts')
