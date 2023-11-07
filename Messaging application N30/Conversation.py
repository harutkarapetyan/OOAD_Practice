
class Conversation:
    def __init__(self, users):
        self.users = users
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)
        for user in self.users:
            if user != message.sender:
                user.receive_message(message)