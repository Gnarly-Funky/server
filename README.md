<a href="https://heroku.com/deploy">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>

![Django](https://img.shields.io/badge/Django-2.2.5-orange) ![Django REST Framework](https://img.shields.io/badge/djangorestframework-3.10.3-brightgreen) ![django-allauth](https://img.shields.io/badge/django--allauth-0.40.0-red) ![python-decouple](https://img.shields.io/badge/python--decouple-3.1-yellow) ![Psycopg2-Binary](https://img.shields.io/badge/psycopg2-2.8.3-lightgrey) ![whitenoise](https://img.shields.io/badge/whitenoise-4.1.4-red) ![django-rest-auth](https://img.shields.io/badge/django--rest--auth-0.9.4-yellowgreen) ![gunicorn](https://img.shields.io/badge/gunicorn-19.9.0-blue) ![Django-Heroku](https://img.shields.io/badge/Django--Heroku-0.3.0-brightgreen)

# GNARLY FUNKY SERVER

This repository contains the server for the Gnarly Funky build week team. This Django server serves up a multiplayer real-time vitual world (MUD) to a client front-end.

## TABLE OF CONTENTS

- [Contributors](#contributors)
- [Technology Stack](#technology-stack)
- [API Endpoints](#api-examples)
  - [Login](#login)
  - [Registration](#registration)
  - [Init](#init)
  - [World](#world)
  - [Move](#move)
- [Data Structures](#data-structures)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## CONTRIBUTORS

- [Christian Allen](https://github.com/christiansallen)
- [Andrew Benedict](https://github.com/atbenedict)
- [Robert Driskell](https://github.com/BobbyAD)
- [Nathan Thomas](https://github.com/nwthomas)

## TECHNOLOGY STACK

The core dependencies are as follows:

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

```json
{
  "username": "mcfly",
  "password1": "wehavetogoback",
  "password2: "wehavetogoback"
}
```

#### Response

##### 200 (OK)

> If you successfully register, the endpoint will return an HTTP response with a status code `200` and a body as below.

```json
{
  "key": "4f5d1b80619c3851e382f34a1d67efdc03c68192639"
}
```

##### 400 (Bad Request)

> If you either try to register with an existing username or submit two passwords that do not match, you will receive a `400` status code and a body that might selectively contain any of the fields below:

```json
{
  "username": ["A user with that username already exists."],
  "password1": ["This password is too common."],
  "password2": ["This field is required."]
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

```json
{
  "username": "mcfly",
  "password": "wehavetogoback"
}
```

#### Response

##### 200 (OK)

> If you successfully login, the endpoint will return an HTTP response with a status code `200` and a body as below.

```json
{
  "key": "4f5d1b80619c3851e382f34a1d67efdc03c68192639"
}
```

##### 401 (Unauthorized)

> If you are missing a username or password for login, the endpoint will return an HTTP response with a status code `400` and a body as below.

```json
{
  "non_field_errors": ["Unable to log in with provided credentials."]
}
```

## **INIT**

### **Serves up initial server data**

_Method Url:_ `/api/adv/init/`

_HTTP method:_ **[GET]**

#### Headers

| name           | type   | required | description              |
| -------------- | ------ | -------- | ------------------------ |
| `Content-Type` | String | Yes      | Must be application/json |

#### Body

> You must send a header with the following in it:

```json
{
  "authorization": "Token 4f5d1b80619c3851e382f34a1d67efdc03c68192639"
}
```

#### Response

##### 200 (OK)

> If you successfully hit this endpoint, it will return the initial starting data for the user.

```json
{
  "player_uuid": "6720e123-53af-4c1d-9305-8asdfc7d842998",
  "room_uuid": "343sdf67-5cb1-4e0c-8c44-bb04a1a7f62a",
  "player_id": 1,
  "player_name": "docbrown",
  "room_id": 1414,
  "room_title": "Musty Cave of Death",
  "room_description": "Marty, we have to go back!"
}
```

##### 401 (Unauthorized)

> If you are missing an authorization token, the endpoint will return an HTTP response with a status code `400` and a body as below.

```json
{
  "non_field_errors": ["Unable to log in with provided credentials."]
}
```

## **WORLD**

### **Serves up initial world data**

_Method Url:_ `/api/adv/world/`

_HTTP method:_ **[GET]**

#### Headers

| name           | type   | required | description              |
| -------------- | ------ | -------- | ------------------------ |
| `Content-Type` | String | Yes      | Must be application/json |

#### Body

> You must send a header with the following in it:

```json
{
  "authorization": "Token 4f5d1b80619c3851e382f34a1d67efdc03c68192639"
}
```

##### 200 (OK)

> If you successfully hit this endpoint, it will return the initial starting world data.

```json
[
  {
    id: 2365,
    uuid: "bba66a41-be85-4822-b914-f35cf0bcaf0f",
    title: "Lost Chamber of Chaos",
    desc:
      "You've entered a large chambers, filled wall to wall with seating. It must have been used for grand debates. This room looks as though it hasn't been used for anything in decades. You find it hard to think. Which way was out, again?",
    touched: true,
    x: 23,
    y: 0,
    north: false,
    south: true,
    east: false,
    west: false
  },
  {
    id: 2366,
    uuid: "67b1dff8-7670-48b7-b4e9-ce05dcba640b",
    title: "Musty Great Room of Ascendance",
    desc:
      "You're in a massive room. Each footsteps echo off distant walls. A musty smell permeates the air around you. Soft choir chanting drifts down from somewhere.",
    touched: true,
    x: 23,
    y: 1,
    north: true,
    south: true,
    east: false,
    west: false
  },
  {
    id: 2367,
    uuid: "6bdd9655-c5ad-46e3-bf15-6433b42b8211",
    title: "Black Shrine of Ascendance",
    desc:
      "In the center of the room stands a grand statue of an ancient goddess. There's almost no light here. Everything is covered in black drapery. Soft choir chanting drifts down from somewhere.",
    touched: true,
    x: 23,
    y: 2,
    north: true,
    south: false,
    east: true,
    west: false
  }
];
```

##### 401 (Unauthorized)

> If you are missing an authorization token, the endpoint will return an HTTP response with a status code `400` and a body as below.

```json
{
  "non_field_errors": ["Unable to log in with provided credentials."]
}
```

## **MOVE**

### **Allows the player to move around the world map**

_Method Url:_ `/api/adv/move/`

_HTTP method:_ **[GET]**

#### Headers

| name           | type   | required | description              |
| -------------- | ------ | -------- | ------------------------ |
| `Content-Type` | String | Yes      | Must be application/json |

#### Body

> You must send a header with the following in it:

```json
{
  "authorization": "Token 4f5d1b80619c3851e382f34a1d67efdc03c68192639"
}
```

> You must also send a body with a `room_id` number in it:

```json
{
  "room_id": 1567
}
```

#### Response

##### 200 (OK)

> If you successfully hit this endpoint, it will return the `room_id` back along with data about placement of other users on the world map.

```json
{
  "new_room": 2674,
  "other_players": [
    {
      "username": "xxx360_no_scopexxx",
      "room_x": 21,
      "room_y": 7
    },
    {
      "username": "killer_sword",
      "room_x": 20,
      "room_y": 20
    },
    {
      "username": "thomasnw",
      "room_x": 23,
      "room_y": 0
    },
    {
      "username": "johnnyboy",
      "room_x": 23,
      "room_y": 15
    },
    {
      "username": "GyorgLopez",
      "room_x": 20,
      "room_y": 24
    },
    {
      "username": "derp70",
      "room_x": 25,
      "room_y": 16
    },
    {
      "username": "littlebillybob",
      "room_x": 20,
      "room_y": 20
    }
  ]
}
```

##### 401 (Unauthorized)

> If you are missing an authorization token, the endpoint will return an HTTP response with a status code `400` and a body as below.

```json
{
  "non_field_errors": ["Unable to log in with provided credentials."]
}
```

## DATA STRUCTURES

Our data modeling for our world uses a combination of the following two data structures:

1. Matrix
2. Linked List

We build our world using a 2D matrix with `x` and `y` coordinates. However, each nodes contains references to whether or not you can head in a north, south, east, or west direction. The combination of these two data structures gives us the power of a linked list with the `O(1)` lookup time that a matrix of `x` and `y` points affords us.

## LICENSE

[MIT](LICENSE)

## ACKNOWLEDGEMENTS

- Thanks to the entire Lambda School team for the training and education we've received here. It's been top-notch.
