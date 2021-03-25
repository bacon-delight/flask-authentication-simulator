# Flask APIs

This repository contains a set of APIs used by multiple UI projects to demonstrate basic API usage. This is basically a sort of broker for the JSONPlaceholder APIs, adding a layer of authentication to them. While this repository has a limited number of routes at present, I'm occasionally working on expanding the scope of it.

Application Root Deployed at https://bacon-delight-demo-flask-apis.herokuapp.com/

Data Sourced from [{JSON}Placeholder](https://jsonplaceholder.typicode.com/)

#### Available Methods

-   GET
-   POST
-   PUT
-   Basic Authentication
-   Access & Refresh Token Generation
-   Refreshing Access Tokens
-   Params Support - coming soon

#### Examples

-   [Todos](https://jsonplaceholder.typicode.com/todos)
-   [Posts](https://jsonplaceholder.typicode.com/posts)

#### Resources

-   [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/b9de29a0a046ce29d82c)
-   [API Documentation](https://documenter.getpostman.com/view/3672841/TzCHCAr2)

## Getting Started

### Environment Setup

-   Verify that you have [Python](https://www.python.org/downloads/) and your `pip -V` command points to that version
-   Set up a new Python Virtual Environment using [pip](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) or [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

### Repository Setup

After cloning or downloading the repository,

-   Create a new file `.flaskenv` with the following contents (and feel free to change them according to your needs):

```
FLASK_APP=app
FLASK_ENV=development
FLASK_DEBUG=true
FLASK_RUN_PORT=8080
```

-   Run the flask server using `flask run` and the server will be up and running at the specified port in `.flaskenv`
