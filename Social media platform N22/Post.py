from abc import abstractmethod
from datetime import datetime

class Post:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.post_time = datetime.now()
        self.comments = []
        self.likes = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_like(self, user):
        self.likes.append(user)

    @abstractmethod
    def __str__(self):
        pass

class TextPost(Post):
    def __str__(self):
        return f"{self.user.name} - {self.post_time}: {self.content}"

class PhotoPost(Post):
    def __init__(self, user, content, image_url):
        super().__init__(user, content)
        self.image_url = image_url

    def __str__(self):
        return f"{self.user.name} - {self.post_time}: {self.content}\nImage URL: {self.image_url}"