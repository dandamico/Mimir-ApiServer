from flask import make_response, abort, jsonify, request
from config import db
from models import Endpoint, Training


def getAllEndpoint():

    endpoints = Endpoint.query.order_by(Endpoint.name).all()
    return jsonify(endpoints=[endpoint.serialize() for endpoint in endpoints]) 


def newEndpoint(endpoint):

    training = Training.query.filter(Training.id == endpoint.get("training_id")).one_or_none()
    
    if training is not None:

        if Endpoint.query.filter(Endpoint.name == endpoint.get("name")) is not None:

            newEndpoint =  Endpoint(id = endpoint.get("id"), name = endpoint.get("name"))

            training.endpoints.append(newEndpoint)
            db.session.add(newEndpoint)
            db.session.commit()

            return jsonify(newEndpoint.serialize()), 201

        else:
            abort(409,"Endpoint {name} exists already".format(name= endpoint.get("name")),)
    else:
        abort(409,"Training with this id:{training_id} not exists".format(training_id= id))
        


    

def getEndpointById(id):

    endpoint =  Endpoint.query.join(Training, Training.id == Endpoint.training_id).filter(Endpoint.id == id).one_or_none()

    if endpoint is not None:
        return jsonify(endpoint.serialize())
    else:
        abort(404, "Endpoint not found for Id: {id}".format(id=id),)


def updateEndpoint(id, endpoint):

    
    update_endpoint = Endpoint.query.filter(Endpoint.id == id).one_or_none()

    if update_endpoint is not None:

        data = request.get_json()
        update_endpoint.deserialize(data)
        db.session.commit()
        
        return jsonify(update_endpoint.serialize()), 200

    else:
        abort(404, "Endpoint not found for Id: {id}".format(id = id))


def deleteEndpoint(id):

    endpoint = Endpoint.query.filter(Endpoint.id == id).one_or_none()

    if endpoint is not None:
        db.session.delete(endpoint)
        db.session.commit()

        return make_response(
            "Endpoint with id:{id} successfully deleted".format(id= id), 200
        )

    else:
        abort(
            404, "Endpoint with this id: {id} not found".format(id= id)
        )


