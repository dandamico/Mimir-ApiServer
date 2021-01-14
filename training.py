from flask import make_response, abort, jsonify, request
from config import db, app
from models import Training, Endpoint
import os
from os.path import join
from rpc_client import RpcClient

def getAllTraining():

    trainings = Training.query.order_by(Training.id).all()
    return jsonify(trainings=[training.serialize() for training in trainings]) 



def newTraining(name): 
    
    uploaded_file = request.files['file']
      
    newTraining = Training(name = str(name), status = "pending")

    if uploaded_file.filename != '':
                   
        file_path = os.path.join(app.config['PATH_FOLDER'], uploaded_file.filename)

        newTraining.file_path = file_path
        newTraining.file_name = uploaded_file.filename
        
        uploaded_file.save(file_path)

        db.session.add(newTraining)
        db.session.commit()

        request_rpc = RpcClient()
        print(" [x] Requesting creating training")
        
        message = {
            'id': newTraining.id,
            'name': newTraining.name,
            'type': 'Training',
            'action': 'Create',
            'file_path': file_path,
            'file_name': uploaded_file.filename
        }
        
        response = request_rpc.call(message)
        print(" [.] Successfully")

        return jsonify(newTraining.serialize()), 201

    else:
        abort(409,"This is not valid training")


def getTrainingById(id):

    training = Training.query.filter(Training.id == id).outerjoin(Endpoint).one_or_none()

    if training is not None:
        return jsonify(training.serialize())

    else:
        abort(404, "Training not found for Id: {id}".format(id= id),)
 


def updateTraining(id,training):

    
    update_training = Training.query.filter(Training.id == id).one_or_none()
    print(update_training)

    if update_training is not None:

        data = request.get_json()
        print(data)

        update_training.deserialize(data)
        print(update_training)

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
            404, "Training with this id: {id} not found".format(id= id)
        )
