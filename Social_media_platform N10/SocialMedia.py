from Comment import Comment
from abc import ABC
from User import User
from Post import Post

class SocialMedia(ABC):
    def __init__(self):
        self.users = []
        self.posts = []
        self.comments = []

    def create_user(self, name, contact_info):
        user = User(name, contact_info)
        self.users.append(user)
        return user

    def create_post(self, user, content):
        post = Post(user, content)
        self.posts.append(post)
        return post

    def create_comment(self, user, post, content):
        comment = Comment(user, post, content)
        self.comments.append(comment)
        return comment

    def view_posts(self):
        for post in self.posts:
            post.display_post()