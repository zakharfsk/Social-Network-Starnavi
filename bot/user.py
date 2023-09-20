import random

from faker import Faker

from .conf import MAX_POSTS_PER_USER, MAX_LIKES_PER_USER
from .utils import make_request

faker = Faker()


class User:
    """
    A class representing a user of the social network.

    Attributes:
    -----------
    username : str
        The username of the user.
    first_name : str
        The first name of the user.
    last_name : str
        The last name of the user.
    email : str
        The email of the user.
    posts : list
        A list of post ids created by the user.
    liked_posts : list
        A list of post ids liked by the user.
    _password : str
        The password of the user.
    _access_token : str
        The access token of the user.
    _refresh_token : str
        The refresh token of the user.
    _max_likes : int
        The maximum number of likes allowed for the user.
    """

    __slots__ = (
        'username',
        'first_name',
        'last_name',
        'email',
        'posts',
        'liked_posts',
        '_password',
        '_access_token',
        '_refresh_token',
        '_max_likes'
    )

    def __init__(self, username: str, first_name: str, last_name: str, email: str, password: str):
        """
        Constructs a User object.

        Parameters:
        -----------
        username : str
            The username of the user.
        first_name : str
            The first name of the user.
        last_name : str
            The last name of the user.
        email : str
            The email of the user.
        password : str
            The password of the user.
        """
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.liked_posts = []
        self._password = password
        self._access_token = None
        self._refresh_token = None
        self._max_likes = MAX_LIKES_PER_USER

    def signup(self):
        """
        Registers the user to the social network.
        """
        print(f'Signup {self.username} user...')
        make_request('POST', '/account/register/', {
            "username": self.username,
            "password": self._password,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name
        })
        self.login()

    def login(self):
        """
        Logs in the user to the social network.
        """
        print(f'Login {self.username} user...')
        tokens = make_request(
            'POST',
            '/account/login/',
            {"username": self.username, "password": self._password}
        )

        self._access_token = tokens.json()['access']
        self._refresh_token = tokens.json()['refresh']

    def update_tokens(self):
        """
        Updates the access token of the user.
        """
        print('You unauthorized, update tokens...')
        response = make_request(
            'POST',
            '/account/token/refresh/',
            {"refresh": self._refresh_token},
        )

        if response.status_code == 401:
            self.login()

        self._access_token = response.json()['access']

    def create_posts(self):
        """
        Creates posts for the user.
        """
        print(f'Create posts for {self.username}...')
        for _ in range(random.randint(1, MAX_POSTS_PER_USER)):
            post_info = make_request(
                'POST',
                '/posts/create/',
                {
                    "title": faker.sentence(nb_words=10, variable_nb_words=False),
                    "text": faker.text(max_nb_chars=10000),
                },
                headers={'Authorization': f'Bearer {self._access_token}'}
            )

            if post_info.status_code == 401:
                self.update_tokens()
                self.create_posts()

            self.posts.append(post_info.json().get('id'))
            print(f'Create post #{_ + 1}')

    def like_post(self, post_id: int):
        """
        Likes a post by its id.

        Parameters:
        -----------
        post_id : int
            The id of the post to like.
        """
        # Check if the user has reached the maximum number of likes
        if len(self.liked_posts) >= self._max_likes:
            print(f'{self.username} has reached the maximum number of likes ({self._max_likes}). '
                  f'Cannot like post #{post_id}')
            return

        # Check if the user is trying to like their own post
        if post_id in self.posts:
            print(f'{self.username} cannot like their own post #{post_id}')
            return

        # Check if the user has already liked the post
        if post_id in self.liked_posts:
            print(f'{self.username} has already liked post #{post_id}')
            return

        print(f'{self.username} likes post #{post_id}')
        like_info = make_request(
            'POST',
            f'/posts/like/{post_id}/',
            headers={'Authorization': f'Bearer {self._access_token}'}
        )

        if like_info.status_code == 401:
            self.update_tokens()
            self.like_post(post_id)

        self.liked_posts.append(post_id)

    def __str__(self):
        """
        Returns a string representation of the user.
        """
        return f"User {self.username} with {len(self.posts)} posts"

    def __repr__(self):
        """
        Returns a string representation of the user.
        """
        return f"User {self.username} with {len(self.posts)} posts"
