from flask import make_response, abort, jsonify, request
from config import db
from models import Endpoint, Training


def getAllEndpoint():

    endpoints = Endpoint.query.order_by(Endpoint.endpoint_name).all()
    return jsonify(endpoints=[endpoint.serialize() for endpoint in endpoints]) 


def newEndpoint(endpoint):

    training = Training.query.filter(Training.training_id == endpoint.get("training_id")).one_or_none()
    
    if training is not None:
        newEndpoint =  Endpoint(endpoint_id = endpoint.get("endpoint_id"), endpoint_name = endpoint.get("endpoint_name"))

        training.endpoints.append(newEndpoint)
        db.session.add(newEndpoint)
        db.session.commit()

        return jsonify(newEndpoint.serialize()), 201
    else:
        abort(409,"Endpoint {endpoint_name} exists already".format(endpoint_name=endpoint_name),)


    

def getEndpointById(endpoint_id):

    endpoint =  Endpoint.query.join(Training, Training.training_id == Endpoint.training_id).filter(Endpoint.endpoint_id == endpoint_id).one_or_none()

    if endpoint is not None:
        return jsonify(endpoint.serialize())
    else:
        abort(404, "Endpoint not found for Id: {endpoint_id}".format(endpoint_id=endpoint_id),)


def updateEndpoint(endpoint_id, endpoint):

    
    update_endpoint = Endpoint.query.filter(Endpoint.endpoint_id == endpoint_id).one_or_none()

    if update_endpoint is not None:

        data = request.get_json()
        update_endpoint.deserialize(data)
        db.session.commit()
        
        return jsonify(update_endpoint.serialize()), 200

    else:
        abort(404, "Endpoint not found for Id: {endpoint_id}".format(endpoint_id = endpoint_id))


def deleteEndpoint(endpoint_id):

    endpoint = Endpoint.query.filter(Endpoint.endpoint_id == endpoint_id).one_or_none()

    if endpoint is not None:
        db.session.delete(endpoint)
        db.session.commit()

        return make_response(
            "{endpoint_id} successfully deleted".format(endpoint_id=endpoint_id), 200
        )

    else:
        abort(
            404, "Endpoint with this id: {endpoint_id} not found".format(endpoint_id=endpoint_id)
        )


