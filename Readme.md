For a better experience, please view this file using a markdown viewer. <br>

# Django CRUD API

This project aims to retrieve data from an external source, store it in an appropriate database 
structure, and create a CRUD RESTful API to interact with the database.

It uses Django Rest Framework to create the API including the CRUD endpoints. <br>

### Table of Contents
- [Objectives](#objectives)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Technologies](#technologies)
- [Out of Scope](#out-of-scope)

### Objectives

1. Retrieve data from the GraphQL endpoint: <br>
`https://swapi-graphql.netlify.app/.netlify/functions/index ` <br>
using a Modular Query Methodology. <br>
 You can visualize the data shape [here](https://studio.apollographql.com/public/star-wars-swapi/variant/current/explorer).
2. Store the obtained data from the GraphQL endpoint into the database and create appropriate models.
3. Write RESTful Create, Read, Update, and Delete endpoints to interact with the database.

### Requirements
- Poetry is used to manage the dependencies. <br>

### Installation
- Run `poetry install` to install the dependencies.

### Usage
- Run `poetry shell` to activate the virtual environment.
- Run `python manage.py runserver` to start the server.
- Open:
  - [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/) in your browser to view the API.
  - [http://127.0.0.1:8000/api/reset_data/](http://127.0.0.1:8000/api/reset_data/) in your browser to reset the data in the database. Every time 
  this endpoint is called, all records in the database are permanently deleted and recreated with the 
  information from SWAPI.
  - [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) in your browser to view the admin panel.<br>
    (Run `python manage.py createsuperuser` to create a superuser.)

### Endpoints
All endpoints are prefixed with `/api/`. All endpoints adhere to the RESTful API format. <br><br>
List of endpoints:
- **List Endpoint (GET)** - Retrieve a list of all instances of the model. 
    - example: `GET /api/planet/`
- **Detail Endpoint (GET)** - Retrieve details of a specific instance of the model. 
    - example: `GET /api/planet/{pk}`
- **Create Endpoint (POST)** - Create a new instance of the model.
    - example: `POST /api/planet/`
- **Update Endpoint (PUT)** - Update a specific instance of the model using a complete representation.
    - example: `PUT /api/planet/{pk}`
- **Partial Update Endpoint (PATCH)** - Update a specific instance of the model using a partial representation.
    - example: `PATCH /api/planet/{pk}`
- **Delete Endpoint (DELETE)** - Delete a specific instance of the model.
    - example: `DELETE /api/planet/{pk}`

### Technologies
- Python 3.11.3
- Django 4.2.4
- Django REST Framework @latest
- Poetry 1.4.2
- SQLite 
- django_mysql

### Out of Scope
- Authentication and Authorization.
- Testing.
- Deployment.
- Frontend.
- Dockerization.
- CI/CD.
- Documentation.
- Logging.
- Caching.
- Rate Limiting.
- Filtering.
- Versioning.
- Monitoring.
- Security.
- Performance. (partially done)
- Scalability.
