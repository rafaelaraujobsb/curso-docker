from flask import Flask
from flask_restful import Api

from app.api.clientes import Clientes


app = Flask(__name__)
api = Api(app)

api.add_resource(Clientes, '/clientes')
