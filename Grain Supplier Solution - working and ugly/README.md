# Grains REST Django Server

Blue Prism Exercise.

## Requirements

Install Docker.

## How to run

Spin up docker containers

```bash
docker compose up -d --build
```

Then navigate to
* [Browsable REST API](http://localhost:8000/)
* [Django Admin](http://localhost:8000/admin)

Seed some data
```bash
docker exec -it grains_server python manage.py loaddata users usersProfiles suppliers orders
```


## REST Endpoints
| HTTP Method        | Endpoint                     | Notes                                          |
|--------------------|------------------------------|------------------------------------------------|
| GET                | /user/, /users/<id>          | Login required as admin, CRUD not implemented  |
| GET                | /suppliers/, /suppliers/<id> |                                                |
| POST               | /suppliers                   | Login required as supplier                     |
| PUT, PATCH, DELETE | /suppliers/<id>              | Login required as supplier                     |
| GET                | /orders, /orders/<id>        |                                                |
| POST               | /orders/                     | Only customer can post                         |
| PUT, PATCH, DELETE | /orders/<id>                 | Only customers can update, anyone can delete   |
| GET				 | /orders/<id>/fullfill        |                                                |
| PUT                | /orders/<id>/fullfill        | Only broker can fullfill                       |


## User Logins

### Superuser
Login - admin@admin.com
Password - admin

### Supplier
Email - supplier@<city>.com
Password - ILoveDjango

### Customer
Email - customer@<city>.com
Password - ILoveDjango

### Broker
Email - broker@one.com
Password - ILoveDjango
