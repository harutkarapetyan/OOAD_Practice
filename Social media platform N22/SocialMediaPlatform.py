from abc import ABC
from User import User
from Post import TextPost, PhotoPost
from Comment import Comment

class SocialMediaPlatform(ABC):
    def __init__(self):
        self.users = []
        self.posts = []

    def create_user(self, name, contact_info):
        user = User(name, contact_info)
        self.users.append(user)
        return user

    def create_post(self, user, content):
        post = TextPost(user, content)
        self.posts.append(post)
        return post

    def create_photo_post(self, user, content, image_url):
        post = PhotoPost(user, content, image_url)
        self.posts.append(post)
        return post

    def comment_on_post(self, user, post, content):
        comment = Comment(user, post, content)
        post.add_comment(comment)
        return comment

    def like_post(self, user, post):
        post.add_like(user)

    def view_timeline(self, user):
        print(f"{user.name}'s Timeline:")
        for post in self.posts:
            if post.user == user:
                print(post)