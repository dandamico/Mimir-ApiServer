from flask import make_response, abort
from config import db
from models import Training, TrainingSchema


def getAllTraining():

    training = Training.query.order_by(Training.training_name).all()

    n_schema = TrainingSchema(many=True)
    data = n_schema.dump(training)
    return data 


def newTraining(training):

    training_name = training.get("training_name")

    existing_training = Training.query.filter(Training.training_name == training_name).one_or_none()

    
    if existing_training is None:

        schema = TrainingSchema()
        newTraining = schema.load(training)

        # Add the person to the database
        db.session.add(newTraining)
        db.session.commit()

        # Serialize and return the newly created person in the response
        data = schema.dump(newTraining)
        return data, 201

    # Otherwise, nope, person exists already
    else:
        abort(409,"Training {training_name} exists already".format(training_name=training_name),)


def getTrainingById(training_id):

    training = Training.query.filter(Training.training_id == training_id).one_or_none()

    if training is not None:
        t_schema = TrainingSchema()
        data = t_schema.dump(training)
        return data

    else:
        abort(404, "Training not found for Id: {training_id}".format(training_id=training_id),)
    





def updateTraining(training_id,training):

    
    update_training = Training.query.filter(Training.training_id == training_id).one_or_none()

    if update_training is not None:
        schema = TrainingSchema()
        update = schema.load(training)

        update.training_id = update_training.training_id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_training)

        return data, 200

    else:
        abort(404, f"Training not found for Id: {training_id}")


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
