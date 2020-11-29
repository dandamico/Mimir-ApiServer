from flask import make_response, abort, jsonify, request
from config import db
from models import Notebook
from rpc_client import FibonacciRpcClient

def getAllNotebook():

    notebooks = Notebook.query.order_by(Notebook.name).all()   
    return jsonify(notebooks=[notebook.serialize() for notebook in notebooks]) 


def newNotebook(notebook):

    existing_notebook = Notebook.query.filter(Notebook.name == notebook.get("name")).one_or_none()
    
    if existing_notebook is None:

        newNotebook = Notebook(id = notebook.get("id"), name = notebook.get("name"), status= "pending")

        db.session.add(newNotebook)
        db.session.commit()

        #print(" [x] Requesting creating notebook")
        #response = createNotebook(newNotebook)
        
        fibonacci_rpc = FibonacciRpcClient()
        print(" [x] Requesting creating notebook")
        response = fibonacci_rpc.call(newNotebook.id)
        print(" [.] Successfully")
        
        return jsonify(newNotebook.serialize()), 201

    else:
        abort(409,"Notebook {name} exists already".format(name= name),)
        

def getNotebookById(id):

    notebook = Notebook.query.filter(Notebook.id == id).one_or_none()

    if notebook is not None:
        return jsonify(notebook.serialize())
    else:
        abort(404, "Notebook not found for Id: {id}".format(id= id),)
    

def deleteNotebook(id):

    notebook = Notebook.query.filter(Notebook.id == id).one_or_none()

    if notebook is not None:
        db.session.delete(notebook)
        db.session.commit()

        return make_response(
            "Notebook with id:{id} successfully deleted".format(id= id), 200
        )

    else:
        abort(
            404, "Notebook with this id: {id} not found".format(id= id)
        )

def updateNotebook(id,notebook):

    update_notebook = Notebook.query.filter(Notebook.id == id).one_or_none()


    if update_notebook is not None:
        data = request.get_json() 
        
        update_notebook.deserialize(data)
        
        db.session.commit()

        return jsonify(update_notebook.serialize()), 200

    else:
        abort(404, "Notebook not found for Id: {id}".format(id= id),)




