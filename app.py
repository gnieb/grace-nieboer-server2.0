from flask import Flask, jsonify, make_response
from flask_restful import Resource
# from models import Project, ProjectPhoto
from config import app, api, db
from flask_cors import CORS
from sqlalchemy.sql import text

class Home(Resource):
    def get(self):
        return make_response("AYO")
    



api.add_resource(Home, '/')


if __name__ == '__main__':
    app.run(port=5555, debug=True)