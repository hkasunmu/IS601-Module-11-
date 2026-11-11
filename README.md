
# IS601 Module 11 - Calculation Model

## Project Overview

This project builds on my previous Module 9 and
Module 10 assignments. For Module 11, I added
a Calculation model using SQLAlchemy and
Pydantic validation to make sure calculations
are processed correctly.

## Features

- SQLAlchemy Calculation model
- Pydantic input and output validation
- Addition, Subtraction, Multiplication, Division
- Factory Pattern for calculation operations
- Division-by-zero error handling
- PostgreSQL database integration
- Automated testing with pytest
- GitHub Actions CI/CD
- Docker support

## Technologies Used

- Python
- SQLAlchemy
- Pydantic
- PostgreSQL
- pytest
- Docker
- GitHub Actions
- FastAPI

## How to Run the Tests

1. Download or clone the repository.
2. Open the project in VS Code.
3. Install the required packages:

    py -m pip install -r requirements.txt

4. Create a .env file containing your own
   POSTGRES_PASSWORD, PGADMIN_DEFAULT_EMAIL,
   and PGADMIN_DEFAULT_PASSWORD.

5. Start PostgreSQL:

    docker compose up -d db

6. Set DATABASE_URL to connect to PostgreSQL
   on localhost port 5434 using your own password.

7. Run all tests:

    py -m pytest -v

## Testing

The project includes unit tests, validation
tests, and PostgreSQL integration tests.

During local testing, all 22 tests passed.

## GitHub Actions

GitHub Actions is configured to run automated
tests using a PostgreSQL service container.

## Docker Hub

Docker Hub deployment will be configured and
the image link added here after verification.

## GitHub Repository

https://github.com/hkasunmu/IS601-Module-11-

## Reflection

For Module 11, I learned how to create a
Calculation model and validate information
using Pydantic. I also learned how to test
calculations with PostgreSQL and use GitHub
Actions to automate testing.
