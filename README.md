# Three Lions
## About

The main objective of the Three Lions blog is to provide a user-friendly platform for people to discuss the England National Football team and their progress at the World Cup in 2022. The target end user is anyone and everyone who is interested in football, and who has a desire to follow and discuss the progress of England’s progress at the World Cup.

The blog provides functionality that allows the user to create a personal user account. This access thereby permits the user to interact with the forum platform and take part in discussions. End users are able to: 

	- Create posts.
	- Read posts.
	- Update posts - either their own, using the edit post option, or others’, by commenting and/or liking their posts.
	- Delete posts (only those which they have created themselves).

When users decide to create a post, they are prompted to provide a unique title of their choosing, their post content, and an excerpt to contextualise their post.

Once the post has been created, it will be sent for approval by the admin so as to prevent any unsuitable content being published on the forum. Once the posts have been approved, the user will be able to see them on the main post list page. Whilst the post is awaiting approval the user will be made aware by a message in their personal post page.

Three Lions is a Django framework app. The user's post data is stored in a database with PostgreSql, and the app is hosted on Heroku. The Django administration site was utilised to provide admin control in order to monitor forum content, as well as super user control of CRUD operations - including the ability to delete other users’ posts and comments.

Below is the link to the live website:


## Project Planning

The main goal for this project was to create a simple, user-friendly application that provides an accessible and interactive platform for people to discuss the England National Football Team, and their progress at the 2022 World Cup. Features include the ability for users to:

1. Create a personal user account.
	- Permission based activity allows for controlled interactivity with the forum, cultivating a more positive and user-friendly environment.

2. Create their own posts under the name of their user account.
	- The ability to create their own posts gives users a platform to express their views, and promotes healthy discussion.

3. Manage their posted content, with the option to edit and delete their posts.
	- The ability to edit and delete content gives users control over what they post.

4. Have access to read other users’ posts, and the ability to like and comment on these posts.
	- The ability to read and interact with other users’ posts creates a platform for discussion and the building blocks for a community.

5. Admin access to all forum content, controlling what is posted and the ability to delete content after publication.
	- Admin access allows content to be monitored, promoting a positive and safe environment.


The user stories for this project can be viewed [here](https://github.com/ConRdav/pp4-three-lions/projects/1)

## Project Management
I used GitHub's KanBan board to manage my workflow. [Three Lions Workflow](https://github.com/ConRdav/pp4-three-lions/projects/2)

## Features

### Welcome to Three Lions
Upon opening the app users are met with a page full of blog posts which even without an account they can view. 
IMAGE
The navbar for users without an account will have a sign up option allowing them to create their own account.
IMAGE

### Create A Blog Post
Once a user has their account set up they are then given more options on the navbar including 'create a post' and 'My posts'. 
IMAGE

### View Your Own Posts
When a user clicks on my posts they will have a similar screen as the home page but with only their posts on it and it will show if they have been approved by admin or if its pending.
IMAGE


### Delete Your Post
Users will need to confirm they wish to delete their post.
IMAGE


### Edit Your Post
Similar to create your own post form users can alter their previous posts and resubmit them for approval.
IMAGE

## Features left to implement


## Testing

### Automated Testing
I used Django to run automated testing however, sqlite3 was used as a local database to achieve this testing.

* I used Django TestCase to test my forms.py, urls.py and views.py within test_forms.py, test_urls.py and test_views.py.

#### test_forms.py
![testing forms.py]()

#### test_urls.py
![testing urls.py]()

#### test_views.py
![testing views.py]()

* I attempted to test models.py but didn't have a great understanding of what to test for so decided to continue with manual testing for the rest of my app.

#### Django Coverage report
![Coverage report]()
* Using Django Coverage I realised that I hadn't covered enough testing with Django TestCase so manual testing was the next step to cover more testing.

### Manual Testing
* I used a KanBan board to help plan my manual testing and the points I needed to hit. [Here](https://github.com/ConRdav/pp4-three-lions/projects/3)
* Post Model blog posts were ordered by creation date, the blog title is returned and that the like count is returned. ![Post Model]().

* Comment model comments being ordered by creation date, and commenter name was returned along with the comment. ![Comment Model]()

* The paths from url.py that I didn't cover in my automated tested which were users_post, edit_post and delete_post. These links are working.

* If the user isn't logged in they can't create,edit or delete a post and the user can't comment or like a post. The user can view a post and signup or login.![Unregistered User]()

* Logged in users can create, edit and delete their posts. Can comment and like on posts aswell as the ability to sign out.
![Logged in user]()

* Django Admin user can create, edit and delete posts from the Django admin panel, and can approve posts and comments from there too.
![Django Admin]()

### Pep8 and Pylint Python Validators
* admin.py 
* apps.py
* forms.py 
* models.py 
* urls.py
* views.py 
* test_forms.py 
* test_urls.py 
* test_views.py 

### HTML Validation with Official W3C Validator
* base.html
   
* index.html

* create_post.html

* edit_posts.html

* post_detail.html

* user_posts.html
 
* customised version of django-all_auth's login.html

* customised version of django-all_auth's logout.html


* customised version of django-all_auth's signup.html


## Bugs





Existing bugs:



## Deployment




## Used Technologies
* HTML
* CSS
* Python
* JavaScript

## Frameworks and Libraries used
* Django with;
    * gunicorn
    * psycopg2
    * postgresql
    * AllAuth
    * Crispy Forms
    * colorfield
* Bootstrap



## Credits

