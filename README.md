# Pulse - An Open Source Online Learning Platform

*Pulse* is a new (open source) online learning platform, developed to support open education classes taught by [dr. Hannes Datta](https://hannesdatta.com) at Tilburg University.

__The platform is still under development.__

Interested in collaborating? Be in touch via [email](mailto:h.datta@tilburguniversity.edu).

## Features

- Interactive to-do list management
- Discussions centered around the course's learning goals
- Reports on student progress for instructors and students

## Running Pulse

### Login to server

*Pulse* runs on a virtual server in the cloud.

1. Modify permissions of `.pem` credentials file: `chmod 400 credentials.pem`
2. Log on to the remote computer: `ssh -i ec2.pem ubuntu@ec2-XX-XX-XX-XXX.compute-1.amazonaws.com`

Use the `screen -r` command to check whether any software is already running. You can access the particular screen using `screen -r <SCREENNUMBER>`. Exiting is also possible (without closing the session), using `CTRL+A`, and `D`.

### Setup new virtual environment

Setup virtual environment to make sure all packages are installed properly.

```
python3.8 -m venv pulse-env
source pulse-env/bin/activate
python3 -m pip install -r requirements.txt
```

### Directory structure

```
pulse
├── Dockerfile
├── Pipfile
├── README.md
├── api
│   ├── courses.py
│   ├── database.py
│   ├── db.json
│   ├── events_comments.db
│   ├── main.py
│   ├── name.py
│   └── nohup.out
├── docker-compose-old.yml
├── docker-compose.yml
├── myapp
│   └── wsgi.py
├── myproject.ini
├── myproject.log
├── nohup.out
├── project
│   ├── __init__.py
│   ├── app.py
│   ├── auth.py
│   ├── auth0.py
│   ├── db.sqlite
│   ├── emailtool.py
│   ├── main.py
│   ├── models.py
│   ├── static
│   │   └── logo.png
│   ├── templates
│   │   ├── 404.html
│   │   ├── base.html
│   │   ├── base2.html
│   │   ├── base_bare.html
│   │   ├── categories.html
│   │   ├── comments.html
│   │   ├── courses.html
│   │   ├── courses2.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── modules.html
│   │   ├── profile.html
│   │   ├── signup.html
│   │   ├── todo.html
│   │   ├── todo2.html
│   │   └── update.html
│   └── uwsgi.ini
├── requirements.txt
└── wsgi.py
```

### Starting the apps

Pulse consists of two modules: the frontend (programmed in Flask), and the backend (programmed with FastAPI).

#### Frontend (Flask)

The frontend, by default, runs on port 80.

```
export TSH_email=SECRET_EMAIL_ADRESS_FOR_MAILSERVER (check own computer, printenv)
root@ip-XXX:/home/ubuntu/pulse# ../myenv/bin/uwsgi --ini /home/ubuntu/pulse/myproject.ini
../myenv/bin/uwsgi --ini /home/ubuntu/pulse/myproject.ini
```

Other options are by __not__ relying on the python environment `myenv`, using:

```
uwsgi --http-socket :80 --plugin python3 --module wsgi:app --virtualenv /home/ubuntu/myenv --chdir /home/ubuntu/pulse/
```

Yet another way is to start up the Flask development server, rather than UWSGI.

```
export FLASK_APP=project
export FLASK_DEBUG=1
flask run --port 5000
```

## Backend (FastAPI)

The API, by default, runs on port 8000, on an internal server that can only be reached from within the virtual machine. Add `--host 0.0.0.0` to make available the API to other systems.


```
cd api
sudo uvicorn main:app --reload --host 0.0.0.0
```

The app ideally should run via `gunicorn` for some proper load balancing in the future.

```
gunicorn main:app -w 1 -k uvicorn.workers.UvicornWorker &
```


### Things to remember when starting out "fresh"

Remember to create the database tables!

```
import requests
requests.get('API-IP:8000/create')
requests.get('API-IP:8000/create_comments')
```


### Acknowledgements

The platform has been inspired and built upon the fantastic open source contributions of others.

- [Deployment of Flask Web Apps](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04)
- [Simple Flask Todo App using SQLAlchemy and SQLite database](https://github.com/python-engineer/flask-todo)
- Styling by [semantic-ui](https://semantic-ui.com/)
- [Flask Authentication Flow](https://github.com/do-community/flask_auth_scotch) and [this blog post](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login)
- Amazing [Confetti Effects](https://github.com/catdad/canvas-confetti) when completing to do items
