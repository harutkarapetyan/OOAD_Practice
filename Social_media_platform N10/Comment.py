from datetime import datetime

class Comment:
    def __init__(self, user, post, content):
        self.user = user
        self.post = post
        self.content = content
        self.timestamp = datetime.now()
