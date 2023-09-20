import environ

env = environ.Env(
    NUMBER_OF_USER=int,
    MAX_POSTS_PER_USER=int,
    MAX_LIKES_PER_USER=int,
)

environ.Env.read_env('.env')

NUMBER_OF_USER = env('NUMBER_OF_USER')
MAX_POSTS_PER_USER = env('MAX_POSTS_PER_USER')
MAX_LIKES_PER_USER = env('MAX_LIKES_PER_USER')

