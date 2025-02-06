# Tweeter - Mini Blog

This is a microblogging application built using Flask, SQLAlchemy, and Bootstrap. It allows users to register, log in, create posts, follow other users, and explore posts. This project serves as a foundational learning tool for Flask web development.

## Features

- **User Authentication**: Sign up, log in, and log out.
- **User Profiles**: View and edit user profiles.
- **Post Creation**: Create and delete posts.
- **Following System**: Follow/unfollow users.
- **Explore Feed**: View posts from all users.

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Virtual environment (optional but recommended)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/tweeter-mini-blog.git
   cd tweeter-mini-blog
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```
5. Run the application:
   ```bash
   flask run
   ```

## Configuration
Modify `config.py` for database settings, secret keys, and other configurations.

## Deployment
To deploy on a production server:
- Use **Gunicorn** or **uWSGI** as a WSGI server.
- Set up a **PostgreSQL** or **MySQL** database for production.
- Configure **nginx** or **Apache** as a reverse proxy.

## Contributing
Contributions are welcome! Please submit a pull request with detailed changes.
