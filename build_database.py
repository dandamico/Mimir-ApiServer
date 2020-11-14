import os
from config import db
import config
from models import Notebook, Training, Endpoint
from datetime import datetime


NOTEBOOKS = []
	
TRAININGS = []

ENDPOINTS = []

config.createDB()

db.create_all()

for notebook in NOTEBOOKS:
	n = Notebook(id = notebook.get("id"), name = notebook.get("name"))
	db.session.add(n)

for training in TRAININGS:
	t = Training(id = training.get("training_id"), name = training.get("name"))
	for endpoint in training.get("endpoints"):
		endpoint_id, endpoint_name, createdDate = endpoint
		n.endpoints.append(Ednpoint(id= endpoint_id, name= endpoint_name, created_date=datetime.strptime(created_date, "%Y-%m-%d %H:%M:%S")))
	db.session.add(t)

for endpoint in ENDPOINTS:
	e = Endpoint(id = endpoint.get("id"), name = endpoint.get("name"))
	db.session.add(e)

db.session.commit()