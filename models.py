from datetime import datetime
from config import db
from config import ma

class Notebook(db.Model):
	__tablename__= "notebook"
	notebook_id = db.Column(db.Integer, primary_key=True)
	notebook_name = db.Column(db.String(120))
	createdDate = db.Column( db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class NotebookSchema(ma.Schema):
	class Meta:
		model = Notebook
		sqla_session = db.session
