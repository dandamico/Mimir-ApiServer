import os
import connexion
from flask_sqlalchemy import SQLAlchemy
import mysql.connector as mysql

MYSQL_HOST=os.environ.get("MYSQL_HOST")
MYSQL_PSSW=os.environ.get("MYSQL_PASSWORD")
MYSQL_USER=os.environ.get("MYSQL_USER")
MYSQL_URL=os.environ.get("MYSQL_URL")
PATH_FOLDER = os.environ.get("PATH_FOLDER")



basedir = os.path.abspath(os.path.dirname(__file__))

connex_app = connexion.App(__name__,specification_dir=basedir)

app = connex_app.app


def createDB():
	db = mysql.connect(
		host=MYSQL_HOST,
		user=MYSQL_USER,
		passwd=MYSQL_PSSW
		
		)
	cursor = db.cursor()
	cursor.execute("CREATE DATABASE IF NOT EXISTS mimir")

app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = MYSQL_URL+"mimir"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['UPLOAD_FOLDER']= PATH_FOLDER
db = SQLAlchemy(app)

