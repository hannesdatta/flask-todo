# Pulse - An Open Source Online Learning Platform

*Pulse* is a new (open source) online learning platform, developed to support open education classes taught by [dr. Hannes Datta](https://hannesdatta.com) at Tilburg University.

__The platform is still under development.__

## Features

- Interactive to-do list management
- Discussions centered around the course's learning goals
- Reports on student progress for instructor and students


# Launch of prototype

## Setup virtual environment

```
python3.8 -m venv pulse-env
source pulse-env/bin/activate
python3 -m pip install -r requirements.txt
```

## Start Flask app (frontend)

```
uwsgi --http-socket :5000 --plugin python3 --module main:app --virtualenv /home/ubuntu/myenv --chdir /home/ubuntu/pulse/project
```

It is also possible to start up the Flask development server.

```
export FLASK_APP=project
export FLASK_DEBUG=1
flask run --port 5000
```

## Start FastAPI (backend)

```
cd api
uvicorn main:app --reload

```


### Acknowledgements

The platform has been inspired and built upon the fantastic open source contributions of others.

- [Deployment of Flask Web Apps](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04)
- [Simple Flask Todo App using SQLAlchemy and SQLite database](https://github.com/python-engineer/flask-todo)
- Styling by [semantic-ui](https://semantic-ui.com/)
- [Flask Authentication Flow](https://github.com/do-community/flask_auth_scotch) and [this blog post](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login)
