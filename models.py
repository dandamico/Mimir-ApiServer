from datetime import datetime
from config import db
from typing import List



class Notebook(db.Model):
	__tablename__= "notebook"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120))
	created_date = db.Column( db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
	docker_image_name = db.Column(db.String(120))
	deployment_name = db.Column(db.String(120))
	notebook_url = db.Column(db.String(120))
	status = db.Column(db.String(120))
	
	def serialize(self):
		return {
			"id": self.id,
			"name": self.name,
			"created_date": self.created_date,
			"docker_image_name": self.docker_image_name,
			"deployment_name": self.deployment_name,
			"notebook_url": self.notebook_url,
			"status": self.status
		}

	def deserialize(self, data):
		for field in ['id', 'name', 'created_date', 'docker_image_name', 'deployment_name','notebook_url', 'status']:
			if field in data:
				setattr(self,field, data[field])





class Training(db.Model):
	__tablename__= "training"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120))
	created_date = db.Column( db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
	endpoints = db.relationship("Endpoint", back_populates= "training", cascade= "all, delete, delete-orphan", lazy= 'dynamic')
	status = db.Column(db.String(120))
	
	def serialize(self):
		return {
			"id": self.id,
			"name": self.name,
			"created_date": self.created_date,
			"endpoints_count": self.endpoints.count(),
			"status": self.status
		}

	def deserialize(self, data):
		for field in ['id', 'name', 'created_date', 'endpoints_count', 'status']:
			if field in data:
				setattr(self,field, data[field])




class Endpoint(db.Model):
	__tablename__= "endpoint"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120))
	created_date = db.Column( db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
	training_id = db.Column(db.Integer, db.ForeignKey('training.id'))
	training = db.relationship("Training", back_populates="endpoints")
	status = db.Column(db.String(120))

	def serialize(self):

		return {
			"id": self.id,
			"name": self.name,
			"created_date": self.created_date,
			"training": self.training.serialize(),
			"status": self.status
		}

	def deserialize(self, data):
		for field in ['id', 'name', 'createdDate', 'training_id', 'status']:
			if field in data:
				setattr(self,field, data[field])

