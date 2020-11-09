from flask import make_response, abort, jsonify, request
from config import db
from models import Notebook

def getAllNotebook():

    notebooks = Notebook.query.order_by(Notebook.notebook_name).all()   
    return jsonify(notebooks=[notebook.serialize() for notebook in notebooks]) 


def newNotebook(notebook):

    notebook_name = notebook.get("notebook_name")

    existing_notebook = Notebook.query.filter(Notebook.notebook_name == notebook_name).one_or_none()
    
    if existing_notebook is None:

        newNotebook = Notebook(notebook_id = notebook.get("notebook_id"), notebook_name = notebook.get("notebook_name"))

        db.session.add(newNotebook)
        db.session.commit()

        
        return jsonify(newNotebook.serialize()), 201

    else:
        abort(409,"Notebook {notebook_name} exists already".format(notebook_name=notebook_name),)

def getNotebookById(notebook_id):

    notebook = Notebook.query.filter(Notebook.notebook_id == notebook_id).one_or_none()

    if notebook is not None:
        return jsonify(notebook.serialize())
    else:
        abort(404, "Notebook not found for Id: {notebook_id}".format(notebook_id=notebook_id),)
    

def deleteNotebook(notebook_id):

    notebook = Notebook.query.filter(Notebook.notebook_id == notebook_id).one_or_none()

    if notebook is not None:
        db.session.delete(notebook)
        db.session.commit()

        return make_response(
            "{notebook_id} successfully deleted".format(notebook_id=notebook_id), 200
        )

    else:
        abort(
            404, "Notebook with this name: {notebook_id} not found".format(notebook_id=notebook_id)
        )

def updateNotebook(notebook_id,notebook):

    update_notebook = Notebook.query.filter(Notebook.notebook_id == notebook_id).one_or_none()


    if update_notebook is not None:
        data = request.get_json() 

        
        update_notebook.deserialize(data)
        
        #db.session.merge(update_notebook)
        db.session.commit()

        return jsonify(update_notebook.serialize()), 200

    else:
        abort(404, "Notebook not found for Id: {notebook_id}".format(notebook_id=notebook_id),)




