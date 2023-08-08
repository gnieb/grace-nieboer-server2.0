from flask import Flask, make_response, request
from flask_restful import Resource
from config import app, api, db
from models import Project, ProjectPhoto

from flask_cors import CORS
from sqlalchemy.sql import text

from dotenv import load_dotenv
load_dotenv()

CORS(app, supports_credentials=True) 

class Home(Resource):
    def get(self):
        return make_response("AYO")
    
class Projects(Resource):
    def get(self):

        if len(Project.query.all()) <1:
            return make_response("Nothing to see here yet!", 200)
        
        projects = [p.to_dict(rules=('photo',)) for p in Project.query.all()]
        return make_response(projects, 200)

    def post(self):
        name = request.get_json()['name']
        github = request.get_json()['github']
        descript = request.get_json()['descript']
        demo = request.get_json()['demo']
        try:
            project = Project(
                name=name,
                github=github,
                descript=descript,
                demo=demo
            )
        except:
            return make_response({"error":"Validation Error, 400"}, 400)
        try:
            db.session.add(project)
            db.session.commit()
        except:
            return make_response({"error":"Validation Error, 400"}, 400)
        
        return make_response(project.to_dict(), 201)

    
class ProjectPhotos(Resource):
    def get(self):
        projphotos = [p.to_dict() for p in ProjectPhoto.query.all()]
        return make_response(projphotos, 200)
    
    def post(self):
        name=request.get_json()['name']
        project_id=request.get_json()['project_id']
        try:
            newPhoto = ProjectPhoto(
                name=name,
                project_id=project_id
            )
        except:
            return make_response({"error":"Validation Error, 400"}, 400)
        try:
            db.session.add(newPhoto)
            db.session.commit()
        except:
            return make_response({"error":"Unable to save to the database, 400"}, 400)
        return make_response(newPhoto.to_dict(), 201)
    
api.add_resource(Home, '/')
api.add_resource(Projects, '/projects')
api.add_resource(ProjectPhotos, '/photos')

if __name__ == '__main__':
    app.run(port=5555, debug=True)