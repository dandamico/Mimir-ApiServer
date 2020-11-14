from flask import make_response, abort, jsonify, request
from config import db
from models import Training, Endpoint



def getAllTraining():

    trainings = Training.query.order_by(Training.name).all()
    return jsonify(trainings=[training.serialize() for training in trainings]) 


def newTraining(training):

    existing_training = Training.query.filter(Training.name == training.get("name")).one_or_none()

    
    if existing_training is None:

        newTraining = Training(id = training.get("id"), name = training.get("name"))

        db.session.add(newTraining)
        db.session.commit()

        return jsonify(newTraining.serialize()), 201

    else:
        abort(409,"Training {name} exists already".format(name= training.get("name")),)


def getTrainingById(id):

    training = Training.query.filter(Training.id == id).outerjoin(Endpoint).one_or_none()

    if training is not None:
        return jsonify(training.serialize())

    else:
        abort(404, "Training not found for Id: {id}".format(id= id),)
    


def updateTraining(id,training):

    
    update_training = Training.query.filter(Training.id == id).one_or_none()

    if update_training is not None:
        data = request.get_json()

        update_training.deserialize(data)

        db.session.commit()

        return jsonify(update_training.serialize()), 200

    else:
        abort(404, "Training not found for Id: {id}".format(id= id),)


def deleteTraining(id):

    training = Training.query.filter(Training.id == id).one_or_none()

    if training is not None:
        db.session.delete(training)
        db.session.commit()

        return make_response(
            "Training with id:{id} successfully deleted".format(id= id), 200
        )

    else:
        abort(
            404, "Training with this id: {training_id} not found".format(id= id)
        )
