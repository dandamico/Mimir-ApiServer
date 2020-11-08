from flask import make_response, abort, jsonify, request
from config import db
from models import Training, DeserializeTraining, Endpoint



def getAllTraining():

    trainings = Training.query.order_by(Training.training_name).all()
    return jsonify(trainings=[training.serialize() for training in trainings]) 


def newTraining(training):

    training_name = training.get("training_name")

    existing_training = Training.query.filter(Training.training_name == training_name).one_or_none()

    
    if existing_training is None:

        newTraining = Training(training_id = training.get("training_id"), training_name = training.get("training_name"))

        db.session.add(newTraining)
        db.session.commit()

        return jsonify(newTraining.serialize()), 201

    else:
        abort(409,"Training {training_name} exists already".format(training_name=training_name),)


def getTrainingById(training_id):

    training = Training.query.filter(Training.training_id == training_id).outerjoin(Endpoint).one_or_none()

    if training is not None:
        return jsonify(training.serialize())

    else:
        abort(404, "Training not found for Id: {training_id}".format(training_id=training_id),)
    


def updateTraining(training_id,training):

    
    update_training = Training.query.filter(Training.training_id == training_id).one_or_none()

    if update_training is not None:
        data = request.get_json()

        update_training.deserialize(data)

        db.session.commit()

        return jsonify(update_training.serialize()), 200

    else:
        abort(404, "Training not found for Id: {training_id}".format(training_id=traininig_id),)


def deleteTraining(training_id):

    training = Training.query.filter(Training.training_id == training_id).one_or_none()

    if training is not None:
        db.session.delete(training)
        db.session.commit()

        return make_response(
            "{training_id} successfully deleted".format(training_id=training_id), 200
        )

    else:
        abort(
            404, "Training with this id: {training_id} not found".format(training_id=training_id)
        )
