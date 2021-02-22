# Django Geolocation API

Simple Django Rest Framework app providing a REST API for a geolocations database, retrieving data from external [ipstack API](https://ipstack.com/).

# Getting started

Django geolocations API is hosted on heroku: https://kszczyrbak-django-geolocations.herokuapp.com

# Running the app

There are two ways to run this app - locally or using docker-compose.
First, clone this repo to a directory of your choice. The directory containing this README will be the work directory for all of the CLI commands afterwards.

**You also need your own ipstack API key. You can get one at https://ipstack.com/signup/free**

## Docker

### Requirements

Install Docker for the OS of your choice.

In this directory, create a `docker.env` file, copying the environment variables from the `.env.template` file and filling them according to the instructions in the comments.

**Make sure to put every variable and its value in a separate line!**

Make sure Docker backend is running, then:
```
docker-compose up -d
```

If those commands successfully complete, try out your composed instance at http://localhost:8000/api/locations.

If you can see the BrowsableAPI interface, congrats! You have a running instance of Django Geolocations API.

## Locally

### Requirements

First, install the requirements to the virutal or global Python environment:

`pip install -r requirements.txt`

### Configuration
Before running the Django app, you have to set the configuration variables. The necessary variables are listed in the `.env.template` file. You can either:
* Set the environment variables specified in the template file manually, or
* Use the installed `dotenv` package, to set those variables locally, using the .template file. Make sure that the path to the created .env file in `settings.py load_dotenv` function is correct.

**When using .env, make sure to put every variable and its value in a separate line!**


Then, go back to the project directory, and perform migrations on the database:

```python manage.py migrate```

### Running the server

If this command runs without errors, great! Now, try to run the server. You can either use the built-in webserver:

`python manage.py runserver 8000`

or, but only if you are not on Windows, use the installed Gunicorn WSGI:

`gunicorn django_geolocation.wsgi`

# API Specification

The created API consists of three endpoints:


| URL                   | Verb   | Description                       | Detail param value |
| --------------------- | ------ | --------------------------------- | ------------------ |
| /api/locations        | POST   | Add geolocation data for hostname | n/a                |
| /api/locations/{host} | GET    | Add a new car                     | ipv4, ipv6 or URL  |
| /api/locations/{host} | DELETE | Rate a car                        | ipv4, ipv6 or URL  |


  **This API has disabled trailing slash. When making API calls, make sure to drop the slash at the end!**

# Test data

This repo contains inital test data that automatically loads into the composed Docker instance.

To load the data locally, use:

```python manage.py loaddata data.json```

## Test user

A test user account is included in the test data:

```
"username": "testuser"
"password": "testpassword"
```

For test geolocations, please refer to the `data.json` file.