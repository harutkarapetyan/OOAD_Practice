from Conversation import Conversation
from Message import TextMessage
from validate_decorators import validate_email, validate_non_empty_string

class User:
    @validate_non_empty_string("name")
    @validate_email("contact_info")
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.conversations = []

    def create_conversation(self, users):
        conversation = Conversation(users)
        self.conversations.append(conversation)
        for user in users:
            user.conversations.append(conversation)

    def send_message(self, conversation, content):
        message = TextMessage(self, conversation, content)
        conversation.add_message(message)

    def receive_message(self, message):
        print(f"{message.sender.name} said: {message.content}")
