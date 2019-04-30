from flask import request
from flask_restful import Resource


class Clientes(Resource):
    def get(self):
        print('aaaaa')
        return {"name": "junior"}, 200

    def post(self):
        print(request.json)
        return {'name': 'junior'}

    def put(self):
        pass
