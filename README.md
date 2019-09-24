<a href="https://heroku.com/deploy">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>

![Django](https://img.shields.io/badge/Django-2.2.5-orange) ![Django REST Framework](https://img.shields.io/badge/djangorestframework-3.10.3-brightgreen)

# GNARLY FUNKY SERVER

This repository contains the server for the Gnarly Funky build week team. This Django server serves up a multiplayer real-time vitual world (MUD) to a client front-end.

## TABLE OF CONTENTS

- [Contributors](#contributors)
- [Technology Stack](#technology-stack)
- [API Endpoints](#api-examples)
  - [Login](#login)
  - [Registration](#registration)
- [Project Management](#project-management)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## CONTRIBUTORS

- [Christian Allen](https://github.com/christiansallen)
- [Andrew Benedict](https://github.com/atbenedict)
- [Robert Driskell](https://github.com/BobbyAD)
- [Nathan Thomas](https://github.com/nwthomas)

## TECHNOLOGY STACK

The core dependencies were as follows:

1. [django](https://www.djangoproject.com/)
2. [djangorestframework](https://www.django-rest-framework.org/)
3. [python-decouple](https://github.com/henriquebastos/python-decouple)
4. [django-rest-auth](https://github.com/Tivix/django-rest-auth)
5. [django-allauth](https://github.com/pennersr/django-allauth)
6. [pusher](https://pusher.com/)
7. [django-cors-headers](https://pypi.org/project/django-cors-headers/)
8. [gunicorn](https://gunicorn.org/)
9. [django-heroku](https://github.com/heroku/django-heroku)
10. [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
11. [whitenoise](http://whitenoise.evans.io/en/stable/)

## API ENDPOINTS

## **REGISTRATION**

_Method Url:_ `/api/registration/`

_HTTP method:_ **[POST]**

#### Headers

| name           | type   | required | description              |
| -------------- | ------ | -------- | ------------------------ |
| `Content-Type` | String | Yes      | Must be application/json |

#### Body

| name        | type   | required | description                                          |
| ----------- | ------ | -------- | ---------------------------------------------------- |
| `username`  | String | Yes      | Must match a username in the database                |
| `password1` | String | Yes      | Must match the second password sent with the request |
| `password2` | String | Yes      | Must match the first password sent with the request  |

_example:_

```
{
  "username": "mcfly",
  "password1": "wehavetogoback",
  "password2: "wehavetogoback"
}
```

#### Response

##### 200 (OK)

> If you successfully register, the endpoint will return an HTTP response with a status code `200` and a body as below.

```
{
  "key": "4f5d1b80619c3851e382f34a1d67efdc03c68192639"
}
```

##### 400 (Bad Request)

> If you either try to register with an existing username or submit two passwords that do not match, you will receive a `400` status code and a body that might selectively contain any of the fields below:

```
{
  "username": [
    "A user with that username already exists."
  ],
  "password1": [
    "This password is too common."
  ],
  "password2": [
    "This field is required."
  ]
}
```

## **LOGIN**

### **Logs a user in**

_Method Url:_ `/api/login/`

_HTTP method:_ **[POST]**

#### Headers

| name           | type   | required | description              |
| -------------- | ------ | -------- | ------------------------ |
| `Content-Type` | String | Yes      | Must be application/json |

#### Body

| name       | type   | required | description                                                           |
| ---------- | ------ | -------- | --------------------------------------------------------------------- |
| `username` | String | Yes      | Must match a username in the database                                 |
| `password` | String | Yes      | Must match a password in the database corresponding to above username |

_example:_

```
{
  "username": "mcfly",
  "password": "wehavetogoback"
}
```

#### Response

##### 200 (OK)

> If you successfully login, the endpoint will return an HTTP response with a status code `200` and a body as below.

```
{
  "key": "4f5d1b80619c3851e382f34a1d67efdc03c68192639"
}
```

##### 400 (Bad Request)

> If you are missing a username or password for login, the endpoint will return an HTTP response with a status code `400` and a body as below.

```
{
  "non_field_errors": [
    "Unable to log in with provided credentials."
  ]
}
```

## PROJECT MANAGEMENT

We used [Trello](https://trello.com/) to manage our project. Our Kanban board in it can be found [here](https://trello.com/invite/accept-board).

## LICENSE

[MIT](LICENSE)

## ACKNOWLEDGEMENTS

- Thanks to the entire Lambda School team for the training and education we've received here. It's been top-notch.
