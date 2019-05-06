from flask import request
from flask_restful import Resource
from app.modulo.database import Database

class Clientes(Resource):
    def get(self):
        return Database().get_document('clientes', visible={'_id': 0}), 200

    def post(self):
        r = request.form
        Database().set_document('clientes', {"name": r["name"]})
        return {"status": "200"}, 200

    def put(self):
        pass

class ListaClientes(Resource):
    def get(self, id):
        return [{"name": "pedro"}], 200

    def post(self, id):
        pass

    def put(self):
        pass

    def delete(self, id):
        print(id)
