from abc import ABC, abstractmethod
from datetime import datetime

class Message(ABC):
    def __init__(self, sender, conversation, content):
        self.sender = sender
        self.conversation = conversation
        self.content = content
        self.timestamp = datetime.now()

    @abstractmethod
    def display(self):
        pass

class TextMessage(Message):
    def display(self):
        return f"{self.sender.name} said: {self.content}"

class MultimediaMessage(Message):
    def display(self):
        return f"{self.sender.name} sent a multimedia message"
