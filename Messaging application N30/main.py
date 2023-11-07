from User import User

if __name__ == "__main__":
    user1 = User("Alice", "alice@examplegmail.com")
    user2 = User("Bob", "bob@examplegmail.com")
    user3 = User("Charlie", "charlie@examplegmail.com")

    user1.create_conversation([user2, user3])

    user1.send_message(user1.conversations[0], "Hello, everyone!")
    user2.send_message(user2.conversations[0], "Hi, Alice!")
