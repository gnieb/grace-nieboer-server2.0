# from app import app
# from models import db, Project, ProjectPhoto


# with app.app_context():

#     Project.query.delete();
#     ProjectPhoto.query.delete();
#     db.create_all();

#     print("Creating projects...");

#     capstone = Project(name="Inspired Interiors", github="https://github.com/gnieb/interior-design-board", descript="capstone blah blah blah full stack applications built with react js, flask, python etc etc")
#     print("adding capstone to database")

#     db.session.add(capstone)
#     db.session.commit()


#     # capstonePhoto = ProjectPhoto(name="inspiredintphoto1.png", project_id="2")
#     # db.session.add(capstonePhoto)
#     # db.session.commit()

#     print("ALL DONE!")

    