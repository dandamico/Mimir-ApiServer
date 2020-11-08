from datetime import datetime
from config import db
from typing import List



class Notebook(db.Model):
	__tablename__= "notebook"
	notebook_id = db.Column(db.Integer, primary_key=True)
	notebook_name = db.Column(db.String(120))
	createdDate = db.Column( db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

	
	def serialize(self):
		return {
			"notebook_id": self.notebook_id,
			"notebook_name": self.notebook_name,
			"createdDate": str(datetime.now())
		}

	def deserialize(self, data):
		for field in ['notebook_id', 'notebook_name', 'createdDate']:
			if field in data:
				setattr(self,field, data[field])

class DeserializeNotebook(object):
    def __init__(self, notebooks: List[Notebook]):
        self.notebooks = notebooks



class Training(db.Model):
	__tablename__= "training"
	training_id = db.Column(db.Integer, primary_key=True)
	training_name = db.Column(db.String(120))
	createdDate = db.Column( db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
	endpoints = db.relationship("Endpoint", backref= "training", cascade= "all, delete, delete-orphan", lazy= 'dynamic')
	
	def serialize(self):
		return {
			"training_id": self.training_id,
			"training_name": self.training_name,
			"createdDate": str(datetime.now()),
			"endpoints_count": self.endpoints.count()
		}

	def deserialize(self, data):
		for field in ['training_id', 'training_name', 'createdDate']:
			if field in data:
				setattr(self,field, data[field])

class DeserializeTraining(object):
    def __init__(self, trainings: List[Training]):
        self.trainings = trainings



class Endpoint(db.Model):
	__tablename__= "endpoint"
	endpoint_id = db.Column(db.Integer, primary_key=True)
	endpoint_name = db.Column(db.String(120))
	createdDate = db.Column( db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
	training_id = db.Column(db.Integer, db.ForeignKey('training.training_id'))

	def serialize(self):
		return {
			"endpoint_id": self.endpoint_id,
			"endpoint_name": self.endpoint_name,
			"createdDate": str(datetime.now()),
			"training_id": self.training_id
		}

	def deserialize(self, data):
		for field in ['endpoint_id', 'endpoint_name', 'createdDate']:
			if field in data:
				setattr(self,field, data[field])

class DeserializeEndpoint(object):
    def __init__(self, endpoints: List[Endpoint]):
        self.endpoints = endpoints