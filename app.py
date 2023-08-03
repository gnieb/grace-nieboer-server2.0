from flask import Flask, jsonify, make_response
from flask_restful import Resource
from config import app, api, db
from models import Project, ProjectPhoto

from flask_cors import CORS
from sqlalchemy.sql import text

from dotenv import load_dotenv
load_dotenv()

CORS(app, supports_credentials=True) 


# @app.route('/')
# def testdb():
#     try:
#         db.session.query(text('1')).from_statement(text('SELECT 1')).all()
#         return '<h1>It works.</h1>'
#     except Exception as e:
#         # e holds description of the error
#         error_text = "<p>The error:<br>" + str(e) + "</p>"
#         hed = '<h1>Something is broken.</h1>'
#         return hed + error_text

class Home(Resource):
    def get(self):
        return make_response("AYO")
    
class Projects(Resource):
    def get(self):

        if len(Project.query.all()) <1:
            return make_response("Nothing to see here yet!", 200)
        projects = [p.to_dict() for p in Project.query.all()]
        return make_response(projects, 200)
    
class ProjectPhotos(Resource):
    def get(self):
        projphotos = [p.to_dict() for p in ProjectPhoto.query.all()]
        return make_response(projphotos, 200)
    
    

api.add_resource(Home, '/')
api.add_resource(Projects, '/projects')
api.add_resource(ProjectPhotos, '/photos')

if __name__ == '__main__':
    app.run(port=5555, debug=True)