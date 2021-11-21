# Pulse - An Open Source Online Learning Platform

*Pulse* is a new (open source) online learning platform, developed to support open education classes taught by [dr. Hannes Datta](https://hannesdatta.com) at Tilburg University.

__The platform is still under development.__

## Features

- Interactive to-do list management
- Ticking of to do's


### Setup
Create project with virtual environment

```console
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
```

Activate it
```console
$ . venv/bin/activate
```

or on Windows
```console
venv\Scripts\activate
```

Install Flask
```console
$ pip install Flask
$ pip install Flask-SQLAlchemy
```

Set environment variables in terminal
```console
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
```

or on Windows
```console
$ set FLASK_APP=app.py
$ set FLASK_ENV=development
```

Run the app
```console
$ flask run
```

### Acknowledgements

The platform has been inspired and built upon the fantastic open source contributions of others.

- [Simple Flask Todo App using SQLAlchemy and SQLite database](https://github.com/python-engineer/flask-todo)
- Styling by [semantic-ui](https://semantic-ui.com/)
- [Flask Authentication Flow](https://github.com/do-community/flask_auth_scotch) and [this blog post](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login)
