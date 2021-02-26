# Flask APIs
This repository contains a set of APIs used by multiple UI projects to demonstrate basic API usage. While this repository has a limited number of routes currently, I'm occasionally working on expanding the scope of it.

#### Available Methods
- GET
- POST
- PUT
- Basic Authentication
- Access & Refresh Token Generation
- Refreshing Access Tokens

#### Examples
- Todos

#### Resources
- [Postman Collection](https://www.getpostman.com/collections/b9de29a0a046ce29d82c)
- API Documentation - Coming Soon


## Getting Started

### Environment Setup
- Verify that you have [Python](https://www.python.org/downloads/) and your `pip -V` command points to that version
- Set up a new Python Virtual Environment using [pip](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) or [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

### Repository Setup
After cloning or downloading the repository,
- Create a new file `.flaskenv` with the following contents (and feel free to change them according to your needs):
```
FLASK_APP=app
FLASK_ENV=development
FLASK_DEBUG=true
FLASK_RUN_PORT=8080
```
- Run the flask server using `flask run` and the server will be up and running at the specified port in `.flaskenv`