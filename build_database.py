import os
from config import db
from models import Notebook, Training, Endpoint
from datetime import datetime

NOTEBOOKS = []
	
TRAININGS = []

ENDPOINTS = []

if os.path.exists("mimir.db"):
	os.remove("mimir.db")

db.create_all()

for notebook in NOTEBOOKS:
	n = Notebook(notebook_id = notebook.get("notebook_id"), notebook_name = notebook.get("notebook_name"))
	db.session.add(n)

for training in TRAININGS:
	t = Training(training_id = training.get("training_id"), training_name = training.get("training_name"))
	for endpoint in training.get("endpoints"):
		endpoint_name, createdDate = endpoint
		n.endpoints.append(Ednpoint(endpoint_name= endpoint_name, createdDate=datetime.strptime(createdDate, "%Y-%m-%d %H:%M:%S")))
	db.session.add(t)

for endpoint in ENDPOINTS:
	e = Endpoint(endpoint_id = endpoint.get("endpoint_id"), endpoint_name = endpoint.get("endpoint_name"))
	db.session.add(e)

db.session.commit()