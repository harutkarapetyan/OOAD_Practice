from datetime import datetime


class Comment:
    def __init__(self, user, post, content):
        self.user = user
        self.post = post
        self.content = content
        self.comment_time = datetime.now()

    def __str__(self):
        return f"{self.user.name} commented on {self.post.user.name}'s post: {self.content}"
