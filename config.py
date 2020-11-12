import os
import connexion
from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import create_engine
import mysql.connector as mysql
basedir = os.path.abspath(os.path.dirname(__file__))

connex_app = connexion.App(__name__,specification_dir=basedir)

app = connex_app.app

sqlite_url = 'mysql+pymysql://root:0satellite0@localhost/mimir'

def createDB():
	if os.path.exists("mimir.db"):
		os.remove("mimir.db")

	else:	
		db = mysql.connect(
			host= "localhost",
			user = "root",
			passwd="0satellite0"
			)

		cursor = db.cursor()

		cursor.execute("CREATE DATABASE mimir")



#engine = create_engine(sqlite_url)
'''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '0satellite0'
app.config['MYSQL_DB'] = 'mimir'
'''
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

