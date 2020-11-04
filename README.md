# Mimir API-Server

## Getting Started

### Requirements
This project needs 'pipenv' :
```
pip install pipenv
pip install connexion
pip install connexion[swagger-ui]
```

### Setup and launch
Setup the environment and launch the server with the following (you can add `-v` and `-d` to connexion for more verbose output):
```
pipenv install
pipenv shell
connexion run --mock all openapi.yml
```
The API server is up and running, with mocked responses where implementation is not available. 
Browse to [http://localhost:5000/api/ui](http://localhost:5000/api/ui) to access SwaggerUI.
