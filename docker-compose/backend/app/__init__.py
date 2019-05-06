from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from app.api.clientes import Clientes, ListaClientes


app = Flask(__name__)
ccors = CORS(app, resources={r"/clientes/*": {"origins": "*"}})
api = Api(app)

api.add_resource(Clientes, '/clientes/')
api.add_resource(ListaClientes, '/clientes/<string:id>')
