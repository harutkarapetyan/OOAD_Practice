from SocialMedia import SocialMedia

if __name__ == "__main__":
    
    social_media = SocialMedia()
    user1 = social_media.create_user("Alice", "alice@examplegmail.com")
    user2 = social_media.create_user("Bob", "bob@examplegmail.com")

    post1 = social_media.create_post(user1, "Hello, this is my first post!")
    post2 = social_media.create_post(user2, "I'm enjoying this social media platform!")

    comment1 = social_media.create_comment(user2, post1, "Nice post, Alice!")
    comment2 = social_media.create_comment(user1, post2, "Glad to hear that, Bob!")

    social_media.view_posts()

    