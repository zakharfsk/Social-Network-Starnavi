## Social Network Starnavi

#### Stack

1. Python
2. Django
3. Django REST Framework
4. PostgreSQL
5. Docker Compose

### Installation

1. Clone repository

```bash
git clone https://github.com/zakharfsk/Social-Network-Starnavi.git
```

2. Create virtual environment

```bash
python -m pip install virtualenv
python -m virtualenv venv
```

3. Install requirements

```bash
pip install -r requirements.txt
```

4. Create .env file and add variables

```text
DEBUG=True
SECRET_KEY=django-insecure-ci20ef-n^k-ct!5bwf-3upgjy-5t92ys$9+2&7p=43q)2#$kfj

DATABASE_NAME=social_network_db
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=localhost
DATABASE_PORT=15432

ACCESS_TOKEN_LIFETIME=2
REFRESH_TOKEN_LIFETIME=7

NUMBER_OF_USER=2
MAX_POSTS_PER_USER=5
MAX_LIKES_PER_USER=5
```

5. Start Docker Compose

```bash
docker compose up -d
```

6. Run migrations

```bash
python manage.py migrate
```

7. Run server

```bash
python manage.py runserver
```

8. Run script bot

```bash
python run_bot.py
```

### API Documentation
To view the documentation, you need to go to the address: http://localhost:8000/api/docs/
