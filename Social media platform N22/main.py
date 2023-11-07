from SocialMediaPlatform import SocialMediaPlatform

if __name__ == "__main__":
    social_media = SocialMediaPlatform()

    user1 = social_media.create_user("User 1", "user1@examplegmail.com")
    user2 = social_media.create_user("User 2", "user2@examplegmail.com")

    user1.add_friend(user2)
    user2.add_friend(user1)

    post1 = user1.create_post(social_media, "Hello, world!")
    post2 = user2.create_photo_post(social_media, "My awesome photo!", "example.com/photo.jpg")

    user1.comment_on_post(social_media, post2, "Great photo!")
    user2.like_post(social_media, post1)

    social_media.view_timeline(user2)


