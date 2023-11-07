from validate_decorators import validate_email, validate_non_empty_string

class User:
    @validate_non_empty_string("name")
    @validate_email("contact_info")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.posts = []
        self.friends = []

    def create_post(self, platform, content):
        post = platform.create_post(self, content)
        self.posts.append(post)
        return post

    def create_photo_post(self, platform, content, image_url):
        post = platform.create_photo_post(self, content, image_url)
        self.posts.append(post)
        return post

    def comment_on_post(self, platform, post, content):
        comment = platform.comment_on_post(self, post, content)
        return comment

    def like_post(self, platform, post):
        platform.like_post(self, post)

    def add_friend(self, user):
        self.friends.append(user)