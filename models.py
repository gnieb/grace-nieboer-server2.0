from sqlalchemy_serializer import SerializerMixin
from config import db

class Project(db.Model, SerializerMixin):
    __tablename__ = 'projects'

    serialize_rules = ('-photos',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String )
    github_fe = db.Column(db.String)
    github_be = db.Column(db.String)
    demo = db.Column(db.String)
    descript = db.Column(db.String)
    bullet1 = db.Column(db.String)
    bullet2 = db.Column(db.String)
    bullet3 = db.Column(db.String)
    back_end = db.Column(db.String)
    front_end = db.Column(db.String)
    css = db.Column(db.String)
    database = db.Column(db.String)
   
    photos = db.relationship('ProjectPhoto', back_populates='project')

class ProjectPhoto(db.Model, SerializerMixin):
    __tablename__ = 'projectphotos'
    serialize_rules = ('-project',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    caption = db.Column(db.String)
    url = db.Column(db.String, nullable=False) # This field will store the image file name or path.
    isPhoto = db.Column(db.Boolean)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    
    project = db.relationship('Project', back_populates='photos')