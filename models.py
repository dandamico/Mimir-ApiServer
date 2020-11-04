from datetime import datetime
from config import db, ma
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class Notebook(db.Model):
	__tablename__= "notebook"
	notebook_id = db.Column(db.Integer, primary_key=True)
	notebook_name = db.Column(db.String(120))
	createdDate = db.Column( db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class NotebookSchema(ma.SQLAlchemyAutoSchema):

	class Meta:
		model = Notebook
		sqla_session = db.session
		load_instance = True
		include_relationships = True


class Training(db.Model):
	__tablename__= "training"
	training_id = db.Column(db.Integer, primary_key=True)
	training_name = db.Column(db.String(120))
	createdDate = db.Column( db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class TrainingSchema(ma.SQLAlchemyAutoSchema):

	class Meta:
		model = Training
		sqla_session = db.session
		load_instance = True
		include_relationships = True


class Endpoint(db.Model):
	__tablename__= "endpoint"
	endpoint_id = db.Column(db.Integer, primary_key=True)
	endpoint_name = db.Column(db.String(120))
	createdDate = db.Column( db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class EndpointSchema(ma.SQLAlchemyAutoSchema):

	class Meta:
		model = Endpoint
		sqla_session = db.session
		load_instance = True
		include_relationships = True