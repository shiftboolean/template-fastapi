# <Project Name> Backend API 🎈

![Current Release Version](https://img.shields.io/badge/Release-0.0.1-brightgreen?style=for-the-badge)
![Code Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen?style=for-the-badge)
![Test Cases](https://img.shields.io/badge/Tests-100%25-brightgreen?style=for-the-badge)
[![TeamCity](https://img.shields.io/teamcity/https/teamcity.url.com/e/badge.svg?style=for-the-badge&logo=teamcity)](https://teamcity.url.com/viewType.html?buildTypeId=<project_id>)

## Introduction 📚

This project is the back-end API for the <Project Name> application. It's built with FastAPI and follows a modular monolith architecture. The application handles functionalities such as User Management, Social Media, Shop.

## Deployment Details 🚀

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Snyk Security](https://img.shields.io/static/v1?message=Protected&logo=snyk&labelColor=white&color=green&logoColor=4C4A73&label=%20SNYK&style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

## Getting Started 🚦

Here are the instructions on how to setup this project in your local machine for development and testing purposes.

### Prerequisites

- Python 3.11 or above (recommended 3.11)
- Pip, the Python package installer
- Virtual environment (either virtualenv or Pipenv)
- An IDE (recommended: PyCharm or VSCode)
- For Windows users, Python should be added to the PATH and the command prompt should be used for the commands below.

### Installation

#### Virtual Environment Setup

For macOS and Linux:

```shell
# Create a virtual environment for Python 3.11
python3.11 -m venv ~/.venvs/my-venv-name

# Activate the virtual environment
source ~/.venvs/my-venv-name/bin/activate

# Check the Python version inside the venv
python -V

# Install all dependencies 
pip install -r requirements.txt

```
For Windows:

```shell
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
.\.venv\Scripts\activate

# Check the Python version inside the venv
python -V

# Install all dependencies 
pip install -r requirements.txt

```

Pipenv Setup
```shell
# Create a pipenv environment for Python 3
pipenv --three

# Activate the pipenv environment
pipenv shell

# If you have multiple Python 3 versions installed
pipenv install -d --python 3.9

# Install all dependencies (include -d for installing dev dependencies)
pipenv install -d

```

Usage 💻
After starting the server, you can access the API at `http://localhost:8000/`. The API documentation can be accessed at `http://localhost:8000/docs`.


## Project Structure 🏗️

The application follows a modular structure. Each module encapsulates a business capability and is self-contained. The modules interact with each other through well-defined interfaces.

Here's a brief description of the existing modules:

- `user`: Handles user-related functionalities such as registration, authentication, and profile management.
- `social`: Manages social networking features like posts, comments, and likes.
- `shop`: Handles shop-related functionalities such as product listing, orders, and payments.

Each module has the following structure:

- `models.py`: Defines the database models for the module.
- `schemas.py`: Defines the Pydantic schemas for data validation and serialization.
- `services.py`: Contains the business logic of the module.
- `routes.py`: Defines the API routes of the module.

To add a new module, create a new directory under `app/modules` with the structure described above. Then, import and include the module's routes in `app/api/routes.py`.

## Testing 🧪

**Is Testing important ? Answer is Yes**
Developer don't know which part of our codebase may break! 
We use unit tests mostly for a single purpose. 
It works as documentation, By designing a unit test We help fellow developers, 
how exactly this new feature should work.
For more info read [here](https://sbwiki.atlassian.net/wiki/spaces/GTCRM/pages/2898722817/Properly+setup+of+Test+Enviroment)

To run test 

```bash
  pytest -v app/tests
```

## Creating PR for Release

_Update Release version in query parameters_

[Use Query Parameters to fetch Release Pull request Section
](https://github.com/shiftboolean/<reponame>/compare/master...release/1.1.0?template=release_template.md
)

## License 📄

This project is licensed under the [IUL License](LICENSE).
Copyright (c) ShiftBoolean.

## Website 🌐

Visit us at [ShiftBoolean](www.shiftboolean.com)


