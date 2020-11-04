from flask import make_response, abort
from config import db
from models import Endpoint, EndpointSchema


def getAllEndpoint():

    endpoint = Endpoint.query.order_by(Endpoint.endpoint_name).all()

    e_schema = EndpointSchema(many=True)
    data = e_schema.dump(endpoint)
    return data 


def newEndpoint(endpoint):

    endpoint_name = endpoint.get("endpoint_name")

    existing_endpoint = Endpoint.query.filter(Endpoint.endpoint_name == endpoint_name).one_or_none()

    
    if existing_endpoint is None:

        schema = EndpointSchema()
        newEndpoint = schema.load(endpoint)

        # Add the person to the database
        db.session.add(newEndpoint)
        db.session.commit()

        # Serialize and return the newly created person in the response
        data = schema.dump(newEndpoint)
        return data, 201

    # Otherwise, nope, person exists already
    else:
        abort(409,"Endpoint {endpoint_name} exists already".format(endpoint_name=endpoint_name),)


def getEndpointById(endpoint_id):

    endpoint = Endpoint.query.filter(Endpoint.endpoint_id == endpoint_id).one_or_none()

    if endpoint is not None:
        e_schema = EndpointSchema()
        data = e_schema.dump(endpoint)
        return data

    else:
        abort(404, "Endpoint not found for Id: {endpoint_id}".format(endpoint_id=endpoint_id),)
    





def updateEndpoint(endpoint_id,endpoint):

    
    update_endpoint = Endpoint.query.filter(Endpoint.endpointid == endpoint_id).one_or_none()

    if update_endpoint is not None:
        schema = EndpointSchema()
        update = schema.load(endpoint)

        update.endpoint_id = update_endpoint.endpoint_id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_endpoint)

        return data, 200

    else:
        abort(404, f"Endpoint not found for Id: {endpoint_id}")


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
