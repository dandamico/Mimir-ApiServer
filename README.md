# Mimir API-Server

## Getting Started

### Requirements
This project needs 'pipenv' :
```
pip install pipenv
pipenv install --dev
pipenv shell
```
The second command will allow us to download the dependencies our api-server needs.

### Setup and launch mock server
Setup the environment and launch the server with the following (you can add `-v` and `-d` to connexion for more verbose output):
```
connexion run --mock all openapi.yml
```
The mock server is up and running, with mocked responses where implementation is not available. 
Browse to [http://localhost:5001/api/ui](http://localhost:5001/api/ui) to access SwaggerUI.

### Setup and launch api-server
Starting with setting the following environment variables:
```
MYSQL_HOST
MYSQL_USER
MYSQL_PASSWORD
MYSQL_URL (ex. mysql+pymyql://user:password@host/ )
```
The latest will be useful for working with SQLALCHEMY.

Now create the database:
```
python build_database.py
```
To run the API-server:
```
python app.py
```
The API server is up and running. 
Browse to [http://localhost:5001/api/ui](http://localhost:5001/api/ui) to access SwaggerUI.