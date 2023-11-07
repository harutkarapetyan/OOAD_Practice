from datetime import datetime
from abc import ABC, abstractmethod

class IPost(ABC):
    @abstractmethod
    def create_post(self, user, content):
        pass

    @abstractmethod
    def display_post(self):
        pass

class Post(IPost):
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.timestamp = datetime.now()

    def create_post(self, user, content):
        return Post(user, content)

    def display_post(self):
        print(f"{self.user.name} posted on {self.timestamp}: {self.content}")
