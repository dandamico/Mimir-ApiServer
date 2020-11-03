import os
from config import db
from models import Notebook

NOTEBOOKS = [
	{"notebook_name":"FirstNotebook", "notebook_id":"12345"}]

if os.path.exists("mimir.db"):
	os.remove("mimir.db")

db.create_all()

for notebook in NOTEBOOKS:
	n = Notebook(notebook_id = notebook.get("notebook_id"), notebook_name = notebook.get("notebook_name"))
	db.session.add(n)

db.session.commit()