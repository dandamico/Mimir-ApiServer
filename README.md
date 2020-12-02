# Mimir API-Server

## Getting Started

### Requirements
This project needs 'pipenv' :
```
pip install pipenv
pipenv install --dev
pipenv shell
```
The last command will allow us to download the dependencies our api-server needs

### Setup and launch
Setup the environment and launch the server with the following (you can add `-v` and `-d` to connexion for more verbose output):
```
connexion run --mock all openapi.yml
```
The API server is up and running, with mocked responses where implementation is not available. 
Browse to [http://localhost:5001/api/ui](http://localhost:5001/api/ui) to access SwaggerUI.

