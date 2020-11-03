from flask import make_response, abort
from config import db
from models import Notebook, NotebookSchema


def getAllNotebook():
    notebook = Notebook.query.order_by(Notebook.notebook_name).all()

    n_schema = NotebookSchema(many=True)
    data = n_schema.dump(notebook)
    return data 


def newNotebook(notebook):

    notebook_name = notebook.get("notebook_name")

    existing_notebook = Notebook.query.filter(Notebook.notebook_name == notebook_name).one_or_none()

    
    if existing_notebook is None:

        schema = NotebookSchema()
        newNotebook = schema.load(notebook).data

        # Add the person to the database
        db.session.add(newNotebook)
        db.session.commit()

        # Serialize and return the newly created person in the response

        return schema.dump(newNotebook).data, 201

    # Otherwise, nope, person exists already
    else:
        abort(409,"Notebook {notebook_name} exists already".format(notebook_name=notebook_name),)


def getNotebookById(notebook_id):

    notebook = Notebook.query.filter(Notebook.notebook_id == notebook_id).one_or_none()

    if notebook is not None:
        n_schema = NotebookSchema()
        data = n_schema.dump(notebook)
        return data

    else:
        abort(404, "Notebook not found for Id: {notebook_id}".format(notebook_id=notebook_id),)
    





def updateNotebook(notebook_id,notebook):

    
    update_notebook = Notebook.query.filter(Notebook.notebook_id == notebook_id).one_or_none()

    notebook_name = notebook.get("notebook_name")
    notebook_id = notebook.get("notebook_id")


    existing_notebook = (
        notebook.query.filter(Notebook.notebook_name == name)
        .filter (Notebook.notebook_id == id)
        .one_or_none()
        )

    if update_notebook is None:
        abort(404, "Notebook not found for Id: {notebook_id}".format(notebook_id=notebook_id),)
    
    elif ( existing_notebook is not None and existing_notebook.notebook_id != notebook_id):
        abort ( 409, "Notebook {notebook_name} exist already".format(notebook_name=notebook_name),)

    else:
        schema = NotebookSchema()
        update = schema.load(notebook, session=db.session)

        update.notebook_id = update_notebook.notebook_id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update_notebook)

        return data, 200


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
            404, "Notebook with this id: {notebook_id} not found".format(notebook_id=notebook_id)
        )
