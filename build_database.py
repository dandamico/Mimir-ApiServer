import os
from config import db
from models import Notebook, Training, Endpoint

NOTEBOOKS = [
	{"notebook_name":"FirstNotebook", "notebook_id":"12345"}
	]
	
TRAININGS = [
	{"training_name":"FirstTraining", "training_id":"12345"}
	]

ENDPOINTS = [
	{"endpoint_name":"FirstEndpoint", "endpoint_id":"12345"}
	]	

if os.path.exists("mimir.db"):
	os.remove("mimir.db")

db.create_all()

for notebook in NOTEBOOKS:
	n = Notebook(notebook_id = notebook.get("notebook_id"), notebook_name = notebook.get("notebook_name"))
	db.session.add(n)


for training in TRAININGS:
	t = Training(training_id = training.get("training_id"), training_name = training.get("training_name"))
	db.session.add(t)

for endpoint in ENDPOINTS:
	e = Endpoint(endpoint_id = endpoint.get("endpoint_id"), endpoint_name = endpoint.get("endpoint_name"))
	db.session.add(e)


db.session.commit()