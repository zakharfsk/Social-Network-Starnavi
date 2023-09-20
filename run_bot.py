import random

from faker import Faker

from bot.conf import NUMBER_OF_USER, MAX_LIKES_PER_USER
from bot.user import User

faker = Faker()
list_users = []

for _ in range(NUMBER_OF_USER):
    fake_user_profile = faker.profile()
    u = User(fake_user_profile.get('username'),
             fake_user_profile.get('name').split()[0],
             fake_user_profile.get('name').split()[1],
             fake_user_profile.get('mail'),
             faker.password(length=12, special_chars=False, upper_case=True))

    u.signup()
    list_users.append(u)

for user in list_users:
    user.create_posts()

for user in list_users:
    # Get a list of all users except the current user.
    other_users = [other_user for other_user in list_users if other_user != user]

    # Like posts from other users.
    for _ in range(MAX_LIKES_PER_USER):
        if not other_users:
            break

        # Get a random post from a random user.
        other_user = random.choice(other_users)
        post_to_like = random.choice(other_user.posts)
        user.like_post(post_to_like)
