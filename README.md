# PetStore API Console Application

## Requirements
Python 3.x and `requests` library.

## Installation
Create an environment
`mamba create -n petstore requests python=3`
OR
Use our yaml file
`mamba create -f petstore.yml -n petstore`
Activate the environment created
`mamba activate petstore`

## Usage
Run `python petstore_cli.py` to execute the application.

## Testing
Run `python -m unittest petstore_cli.py` for unit testing.

## Enterprise Readiness
1. Implement logging and error handling.
2. Add API rate limiting.
3. Use environment variables for API endpoints.
4. Containerize the application using Docker.
5. Include CI/CD pipelines.
6. Ensure code review procedures.
7. Add extensive test coverage.
